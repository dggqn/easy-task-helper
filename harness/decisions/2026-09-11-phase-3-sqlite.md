# Phase 3 SQLite 持久化决策

- 日期：2026-09-11
- 决策：使用 Python 标准库 SQLite 保存任务主记录和阶段事件。
- 原因：单用户桌面应用无需独立数据库服务；SQLite 支持事务、索引、约束和崩溃恢复，后续可扩展命令运行与文件访问审计。
- 数据位置：Windows 使用 `%APPDATA%/eth/data/tasks.db`；不放入用户项目目录，也不提交 Git。
- 取舍：当前不引入 ORM 或第三方依赖，以保持 Python Harness 轻量。
