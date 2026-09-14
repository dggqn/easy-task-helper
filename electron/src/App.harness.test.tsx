import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { afterEach, describe, expect, it } from 'vitest'
import App from './App'

afterEach(() => { delete window.ethHarness })

describe('Python Harness bridge', () => {
  it('renders the structured task result', async () => {
    window.ethHarness = { runTask: async () => ({ task_id: 'task-0001', stage: 'completed', summary: 'Local plan created.', plan: ['Inspect the selected project.'] }) }
    render(<App />); fireEvent.click(screen.getByRole('button', { name: /运营数据控制台/ })); fireEvent.change(screen.getByRole('textbox'), { target: { value: 'Add filtering.' } }); fireEvent.click(screen.getByRole('button', { name: /发送/ }))
    await waitFor(() => expect(screen.getByText(/Local plan created/)).toBeInTheDocument()); expect(screen.getByText(/1\. Inspect the selected project/)).toBeInTheDocument()
  })
  it('can close an action result panel', async () => {
    window.ethHarness = { runTask: async () => ({ task_id: 'task-0001', stage: 'completed', summary: '', plan: [] }), runAction: async () => ({ return_code: 0, output: 'ok' }) }
    render(<App />); fireEvent.click(screen.getByRole('button', { name: /运营数据控制台/ })); fireEvent.click(screen.getByRole('button', { name: '运行测试' })); await waitFor(() => expect(screen.getByRole('region', { name: '执行结果' })).toBeInTheDocument()); fireEvent.click(screen.getByRole('button', { name: '关闭执行结果' })); expect(screen.queryByRole('region', { name: '执行结果' })).not.toBeInTheDocument()
  })
})
