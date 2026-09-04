import { fireEvent, render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import App from './App'

describe('Phase 1 product shell', () => {
  it('selects a project and opens its task page', () => {
    render(<App />)

    fireEvent.click(screen.getByRole('button', { name: /运营数据控制台/ }))

    expect(screen.getByRole('heading', { name: '开发任务' })).toBeInTheDocument()
    expect(screen.getAllByText('运营数据控制台')).not.toHaveLength(0)
    expect(screen.getByText('执行计划中')).toBeInTheDocument()
  })

  it('adds a user task and placeholder response to the conversation', () => {
    render(<App />)
    fireEvent.click(screen.getByRole('button', { name: /运营数据控制台/ }))

    fireEvent.change(screen.getByLabelText('描述功能、问题或验收要求'), {
      target: { value: '增加筛选功能' },
    })
    fireEvent.click(screen.getByRole('button', { name: /发送/ }))

    expect(screen.getByText('增加筛选功能')).toBeInTheDocument()
    expect(screen.getByText(/当前为 Phase 1 占位流程/)).toBeInTheDocument()
  })

  it('returns to the project list', () => {
    render(<App />)
    fireEvent.click(screen.getByRole('button', { name: /运营数据控制台/ }))
    fireEvent.click(screen.getByRole('button', { name: /项目列表/ }))

    expect(screen.getByRole('heading', { name: '选择要继续开发的 Web 项目' })).toBeInTheDocument()
  })
})
