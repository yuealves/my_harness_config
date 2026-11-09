# 文档地图

三个必需目录，各回答一类问题：

- `design/`：系统是什么、为什么这样设计。先读[总体设计](design/0.overview.md)。
- `how-to/`：怎么构建、运行、排查、配置。
- `governance/`：什么不能变，以及怎么检查。

可选目录（用到才建，不建空目录）：

- `validation/`：跨天、全市场或对外验收的记录；设计文档链接它，不复制结论。
- `design/note/`：未定稿的调研和方案过程稿；定稿后并入正式设计或删除。
- `design/archive/`：已被取代的历史方案，保留决策理由，不再更新。

## 按意图找

- 第一次接手：总体设计 → 当前主要模块 → 开发规范。
- 改某个模块：`design/<模块>` → 相关 `governance` 条目。
- 排查问题：`how-to` → `design`（时序、失败处理）→ `governance`。
- 新增能力：`governance` → 相关 `design` → 在 `design/changes/` 建变更文档。

## 正在进行的变更

目前没有进行中的变更。新的需求文档放在 [`design/changes/`](design/changes/README.md)，命名 `YYYY-MM-DD-<主题>.md`；完成后并入对应 Design 并标“已合并”。

## Design

- [0.overview](design/0.overview.md)：<目标、架构、依赖红线和文档地图>
- <模块文档创建后按编号加入：一句话说明>

## How-to

- [1.build-test-run](how-to/1.build-test-run.md)：构建、测试与运行

## Governance

- [coding-standards](governance/coding-standards.md)：C++ / Python 代码规范
- [commit-conventions](governance/commit-conventions.md)：commit message 规范
- [invariants](governance/invariants.md)：正确性不变量
- [ai-workflow](governance/ai-workflow.md)：AI agent 开发守则
