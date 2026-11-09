# 改造既有项目

项目已有代码和文档，要把它们接入本规范时走这条流程。**先审计、再方案、后动手**；没有用户同意不改任何文件。

## 0. 只读审计

先读，不改。至少检查：

- `git status`、`git log --oneline -30`、`git log -5 --format=%B`（类型、scope、语言、正文结构）。
- 目录树、`docs/` 结构、`docs/README.md`、`AGENTS.md`、`README.md`。
- 现有治理文档：代码规范、commit 规范、不变量、AI 规则。
- 格式化与测试配置：`.clang-format`、ruff/black、`pytest.ini`、CMake 测试助手。
- 抽样代码：命名、注释语言、日志宏、错误处理、include 组织。
- 文档健康：死链、超长文档、索引是否覆盖全部文档。

输出差距表：

| 项 | 现状 | 目标 | 动作 |
| --- | --- | --- | --- |
| 文档结构 | <现有目录> | design / how-to / governance | 保留 / 迁移 / 拆分 / 新增 |
| AGENTS.md | <有/无，缺什么> | 入口 + 必读顺序 + 红线 | 重写 / 补丁 |
| 代码规范 | <已有/散落> | governance 四件套 | 新增 / 合并 |
| commit | <历史风格> | Conventional Commits + 英文 | 从下次提交开始执行 |
| 测试 | <框架/标记> | 与规范一致 | 补配置 / 不动 |

## 1. 出方案（等用户同意）

一屏内给出：

- **现状摘要**：3–5 条，只讲影响改造的事实。
- **目标文档树**：用代码块列出改造后的结构。
- **文件动作表**：文件 → 动作（新建 / 迁移 / 拆分 / 合并 / 归档 / 跳过）→ 原因。
- **不动的部分**：代码行为、历史文档内容、用户未提交改动。
- **代码规范落地方式**：配置文件 + 新改动遵守；默认不批量重排格式，不做顺手重构。
- **分阶段 commit 计划**：每阶段一个主题。
- **验证方式**：链接 / 索引检查、构建、测试。
- **待你决定**：≤3 个，各带推荐。

**等用户明确同意后再写；“按推荐来”算同意。**

## 2. 执行顺序

文档规则（通用契约、四类结构、拆分、生命周期、Git 边界）见 `doc-system.md`。

1. **加骨架**：`docs/README.md`、`governance/` 四件套、`design/changes/README.md`；不改旧文档内容。
2. **迁移旧文档**：合并、拆分、归档；每动一篇就修链接和索引，不留死链。
3. **改入口**：`AGENTS.md`、根 `README.md` 对齐新的文档地图和必读顺序。
4. **落代码规范**：`.clang-format`、`pytest.ini`、`tests/test_docs_links.py`；只让新改动遵守，存量在改到时统一。
5. **验证并提交**：每阶段跑链接/索引检查；每个 commit 只做一件事。

## 3. 约束

- 不删技术内容；旧方案归档而不是删除。
- 不改代码行为；不做顺手重构；不批量重排格式，除非用户明确要求。
- 保护用户未提交改动：先看 `git status`，只处理任务文件。
- 文档与代码冲突时以代码为准，并在文档里标出修正。
- 一次改造可以动多篇文档，但按阶段提交，保证每一步可回退。

## 4. 提交建议

```text
docs: add documentation map and governance docs
docs: restructure design docs into hub pages
docs: align AGENTS.md and README with docs-first
chore: add clang-format and docs link test
```
