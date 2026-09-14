import { fireEvent, render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import App from './App'

describe('产品工作台交互', () => {
  function openProject() { render(<App />); fireEvent.click(screen.getByRole('button', { name: /运营数据控制台/ })) }
  it('可以选择项目并返回列表', () => { openProject(); expect(screen.getByRole('heading', { name: '开发任务' })).toBeInTheDocument(); fireEvent.click(screen.getByRole('button', { name: /项目列表/ })); expect(screen.getByRole('heading', { name: '选择要继续开发的 Web 项目' })).toBeInTheDocument() })
  it('进度面板可以展开和收起', () => { openProject(); expect(screen.queryByRole('heading', { name: '执行进度' })).not.toBeInTheDocument(); fireEvent.click(screen.getByRole('button', { name: '查看进度' })); expect(screen.getByRole('heading', { name: '执行进度' })).toBeInTheDocument(); fireEvent.click(screen.getByRole('button', { name: '收起进度' })); expect(screen.queryByRole('heading', { name: '执行进度' })).not.toBeInTheDocument() })
  it('可以发送任务消息', () => { openProject(); fireEvent.change(screen.getByLabelText('描述功能、问题或验收要求'), { target: { value: '增加筛选功能' } }); fireEvent.click(screen.getByRole('button', { name: /发送/ })); expect(screen.getByText('增加筛选功能')).toBeInTheDocument() })
})
