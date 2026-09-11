const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('ethHarness', {
  runTask(payload) {
    return ipcRenderer.invoke('harness:run-task', payload)
  },
  runAction(payload) {
    return ipcRenderer.invoke('harness:action', payload)
  },
})
