import { useMemo, useState } from 'react'
import './App.css'

type Project = { id: string; name: string; path: string; framework: string; status: 'ready' | 'review' }
type Message = { id: string; role: 'assistant' | 'user'; content: string }

const projects: Project[] = [
  { id: 'ops-console', name: '运营数据控制台', path: 'D:\\workspace\\ops-console', framework: 'React + TypeScript', status: 'ready' },
  { id: 'merchant-portal', name: '商家服务门户', path: 'D:\\workspace\\merchant-portal', framework: 'Vue + Vite', status: 'review' },
  { id: 'brand-site', name: '品牌展示站', path: 'D:\\workspace\\brand-site', framework: 'Next.js', status: 'ready' },
]

const initialMessages: Message[] = [{ id: 'welcome', role: 'assistant', content: '项目上下文已加载。描述需要开发或修复的前端功能，我会先建立执行计划。' }]

function App() {
  const [selectedProject, setSelectedProject] = useState<Project | null>(null)
  const [messages, setMessages] = useState<Message[]>(initialMessages)
  const [draft, setDraft] = useState('')
  const [isPanelOpen, setIsPanelOpen] = useState(false)
  const progress = useMemo(() => [
    { label: '需求解析', state: '完成' }, { label: '执行计划', state: '进行中' }, { label: '代码验证', state: '等待' },
  ], [])

  function openProject(project: Project) { setSelectedProject(project); setMessages(initialMessages); setDraft('') }
  async function sendMessage() {
    const content = draft.trim()
    if (!content) return
    const id = Date.now()
    setMessages((current) => [...current, { id: `user-${id}`, role: 'user', content }, { id: `assistant-${id}`, role: 'assistant', content: '已记录这项任务。当前为 Phase 1 占位流程，后续将展示计划、执行和验证结果。' }])
    setDraft('')
    try {
      const result = await window.ethHarness?.runTask({
        project_name: selectedProject?.name ?? '',
        project_path: selectedProject?.path ?? '',
        instruction: content,
      })
      if (!result) return
      setMessages((current) => current.map((message) => message.id === `assistant-${id}` ? {
        ...message,
        content: `${result.summary}\n${result.plan.map((step, index) => `${index + 1}. ${step}`).join('\n')}`,
      } : message))
    } catch (error) {
      const detail = error instanceof Error ? error.message : 'unknown error'
      setMessages((current) => current.map((message) => message.id === `assistant-${id}` ? {
        ...message,
        content: `Harness failed: ${detail}`,
      } : message))
    }
  }

  if (!selectedProject) return <main className="app-shell project-home">
    <header className="topbar"><div className="brand" aria-label="Easy Task Helper"><span className="brand-mark">ETH</span><span>Easy Task Helper</span></div><span className="phase-badge">PHASE 1 / 本地工作台</span></header>
    <section className="project-intro"><p className="eyebrow">DEVELOPMENT ASSISTANT</p><h1>选择要继续开发的 Web 项目</h1><p>从本地项目开始，进入任务对话与执行进度工作台。</p></section>
    <section className="project-list" aria-label="可选择项目">{projects.map((project) => <button className="project-card" key={project.id} type="button" onClick={() => openProject(project)}>
      <span className="project-card-top"><span className={`status-dot ${project.status}`}></span><span>{project.status === 'ready' ? '可开始' : '待复核'}</span></span>
      <strong>{project.name}</strong><span className="project-framework">{project.framework}</span><code>{project.path}</code><span className="project-action">进入任务工作台 <span aria-hidden="true">-&gt;</span></span>
    </button>)}</section>
  </main>

  return <main className="app-shell task-home">
    <header className="topbar"><button className="back-button" type="button" onClick={() => setSelectedProject(null)}><span aria-hidden="true">&lt;-</span> 项目列表</button><div className="brand compact"><span className="brand-mark">ETH</span><span>任务工作台</span></div><button className="outline-button" type="button" onClick={() => setIsPanelOpen((open) => !open)}>{isPanelOpen ? '收起进度' : '查看进度'}</button></header>
    <div className="task-layout">
      <aside className={`project-sidebar ${isPanelOpen ? 'expanded' : ''}`}><p className="eyebrow">CURRENT PROJECT</p><h2>{selectedProject.name}</h2><p className="side-framework">{selectedProject.framework}</p><code>{selectedProject.path}</code><div className="side-divider"></div><p className="side-label">当前任务</p><strong>建立项目功能开发计划</strong><p className="side-copy">占位任务状态，用于验证对话和执行进度流程。</p></aside>
      <section className="conversation" aria-label="任务对话"><div className="conversation-header"><div><p className="eyebrow">TASK CONVERSATION</p><h1>开发任务</h1></div><span className="active-indicator"><span></span> 执行计划中</span></div>
        <div className="message-list">{messages.map((message) => <article className={`message ${message.role}`} key={message.id}><span className="message-role">{message.role === 'assistant' ? 'ETH' : '你'}</span><p>{message.content}</p></article>)}</div>
        <form className="composer" onSubmit={(event) => { event.preventDefault(); sendMessage() }}><label htmlFor="task-input">描述功能、问题或验收要求</label><div className="composer-row"><textarea id="task-input" value={draft} onChange={(event) => setDraft(event.target.value)} placeholder="例如：为数据列表增加按状态筛选能力" rows={3} /><button type="submit" disabled={!draft.trim()}>发送 <span aria-hidden="true">-&gt;</span></button></div></form>
      </section>
      <aside className="progress-panel"><p className="eyebrow">TASK STATUS</p><h2>执行进度</h2><ol>{progress.map((item, index) => <li className={item.state === '进行中' ? 'current' : ''} key={item.label}><span>{String(index + 1).padStart(2, '0')}</span><div><strong>{item.label}</strong><small>{item.state}</small></div></li>)}</ol><div className="progress-note"><span>下一步</span><p>确认任务范围并生成可审查的执行计划。</p></div></aside>
    </div>
  </main>
}

export default App
