const { app, BrowserWindow, ipcMain } = require('electron')
const { execFile } = require('node:child_process')
const path = require('node:path')

const isDevelopment = !app.isPackaged

function runHarnessTask(payload) {
  if (!isDevelopment) return Promise.reject(new Error('当前安装包尚未包含 Python Harness。'))

  const workspacePath = path.resolve(app.getAppPath(), '..')
  const pythonPath = path.join(workspacePath, 'python')
  const args = ['run', '--project', pythonPath, 'eth-harness']

  return new Promise((resolve, reject) => {
    const child = execFile('uv', args, {
      cwd: pythonPath,
      timeout: 30_000,
      env: { ...process.env, PYTHONUTF8: '1' },
    }, (error, stdout, stderr) => {
      if (error) return reject(new Error(stderr.trim() || error.message))
      try {
        resolve(JSON.parse(stdout))
      } catch {
        reject(new Error('Python Harness 返回了无效结果。'))
      }
    })
    child.stdin.end(JSON.stringify(payload))
  })
}

function runHarnessAction(payload) {
  if (!isDevelopment) return Promise.reject(new Error('安装包暂未内置 Python Harness。'))
  const workspacePath = path.resolve(app.getAppPath(), '..')
  const pythonPath = path.join(workspacePath, 'python')
  const safePayload = { ...payload, workspace: workspacePath }
  return new Promise((resolve, reject) => {
    const child = execFile('uv', ['run', '--project', pythonPath, 'eth-harness'], { cwd: pythonPath, timeout: 30_000, env: { ...process.env, PYTHONUTF8: '1' } }, (error, stdout, stderr) => {
      if (error) return reject(new Error(stderr.trim() || error.message))
      try { resolve(JSON.parse(stdout)) } catch { reject(new Error('Python Harness 返回了无效结果。')) }
    })
    child.stdin.end(JSON.stringify(safePayload))
  })
}

function createWindow() {
  const window = new BrowserWindow({
    width: 1360,
    height: 860,
    minWidth: 980,
    minHeight: 680,
    backgroundColor: '#0b1115',
    autoHideMenuBar: true,
    webPreferences: {
      contextIsolation: true,
      nodeIntegration: false,
      preload: path.join(__dirname, 'preload.cjs'),
    },
  })

  if (isDevelopment) {
    window.loadURL('http://127.0.0.1:5173')
  } else {
    window.loadFile(path.join(__dirname, '..', 'dist', 'index.html'))
  }
}

app.whenReady().then(() => {
  ipcMain.handle('harness:run-task', (_event, payload) => runHarnessTask(payload))
  ipcMain.handle('harness:action', (_event, payload) => runHarnessAction(payload))
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})
