# AI Agent 开发守则

所有 AI agent 在本仓库工作前必读：`AGENTS.md` → `docs/README.md` → `docs/design/0.overview.md` → 本目录全部 → 你要修改的模块的设计文档。

## 工作方式

1. **设计文档先行**：新增或大改模块前，先更新对应 `docs/design/` 文档并与用户确认，再写代码。
2. **不做顺手重构**：只改任务要求的范围；发现的无关问题记录并报告，不擅自修改。
3. **每个 commit 自包含验证**：可编译 + 相关测试通过；验证命令见 `AGENTS.md`。
4. **遵守规范**：`coding-standards.md`（代码）、`commit-conventions.md`（提交）、`invariants.md`（正确性）。
5. **不确定就问**：口径、语义、架构取舍上的任何不确定，先问用户，不要自行猜测。

## 禁止事项

- 禁止违反 `invariants.md` 的任何一条（除非用户明确拍板）。
- 禁止未确认就引入新的第三方依赖。
- 禁止修改 `tests/fixtures/` 下的数据文件。
- 禁止 amend / force-push / 提交密钥与内部地址。
- 禁止把大输出命令直接灌进会话：预判超过几百行的命令先重定向到文件，再取摘要。

## 文档义务

- 新增模块：必须有对应 `docs/design/<编号>.<模块>.md`（角色、设计、实现、交互、不变量）。
- 改了模块间交互：同步更新 `docs/design/0.overview.md`。
- 改了规范：同步更新 `docs/governance/` 下对应文档。
