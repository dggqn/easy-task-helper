interface HarnessTaskResult {
  task_id: string
  stage: string
  summary: string
  plan: string[]
}

interface Window {
  ethHarness?: {
    runTask(payload: {
      project_name: string
      project_path: string
      instruction: string
    }): Promise<HarnessTaskResult>
  }
}
