# Commit 规范

Conventional Commits：`<type>(<scope>): <summary>`

## type

| type | 用途 |
| --- | --- |
| feat | 新功能 / 新模块 |
| fix | 修 bug |
| refactor | 不改变行为的重构 |
| perf | 性能优化 |
| test | 测试相关 |
| docs | 纯文档 |
| chore | 构建 / 工具 / 骨架 |

## scope

模块名，按项目实际填写：`<base>` / `<market>` / `<engine>` / `<app>` / `governance` 等。跨模块时可省略。

## 规则

- **summary 与正文一律用英文**；正文里的路径、文档标题等专名保留原文。
- summary 一句话，不超过 72 字符。
- 正文（可选）写设计动机、取舍、验证方式；复杂 commit 用 `Implementation:`、`Validation:` 分段。
- 一个 commit 只做一件事；每个 commit 必须可编译、相关测试通过。
- 禁止 amend 已 push 的 commit；禁止 force-push。
- 禁止夹带与本主题无关的顺手修改。
- 提交前检查 `git diff --cached` 和 `git diff --cached --check`。

## 示例

```text
feat(engine): introduce SymbolWorker and Dispatcher for parallel dispatch

Implementation:
- Dispatcher owns the SharedPayloadRing and all worker rings; appends payloads
  and shards by symbol hash
- SymbolWorker batch-consumes its SPSC ring, decodes, and drives IFamilyWorker

Validation:
- workers=1/4 bitwise-identical output is verified by e2e
```
