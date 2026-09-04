import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { afterEach, describe, expect, it } from 'vitest'
import App from './App'

afterEach(() => {
  delete window.ethHarness
})

describe('Python Harness bridge', () => {
  it('renders the structured result returned through the preload bridge', async () => {
    window.ethHarness = {
      runTask: async () => ({
        task_id: 'task-0001',
        stage: 'completed',
        summary: 'Local plan created.',
        plan: ['Inspect the selected project.'],
      }),
    }
    render(<App />)

    fireEvent.click(screen.getAllByRole('button')[0])
    fireEvent.change(screen.getByRole('textbox'), { target: { value: 'Add filtering.' } })
    const submitButton = screen.getAllByRole('button').find((button) => button.getAttribute('type') === 'submit')
    if (!submitButton) throw new Error('Task submit button was not found.')
    fireEvent.click(submitButton)

    await waitFor(() => expect(screen.getByText(/Local plan created/)).toBeInTheDocument())
    expect(screen.getByText(/1\. Inspect the selected project/)).toBeInTheDocument()
  })
})
