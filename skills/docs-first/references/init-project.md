# 初始化新项目

用户描述一个需求、要建新项目时走这条流程。目标是先立起文档骨架和规范，再写第一版代码；不要从空目录开始堆实现。

## 0. 先对齐（不写文件）

1. 用 2–3 句复述：要解决什么、预期结果、本次范围。
2. 起草六点：业务目的 / 支持场景 / 排除场景 / 不变量 / 失败约定 / 验收依据。
3. 确认项目形态：名称、语言（C++ / Python / 混合）、构建与测试方式、首版模块、目标平台。

每轮最多问 3 个问题，每个给 2–3 个选项、后果和推荐；能从需求推断的不问。只读检查可以直接做。

## 1. 出方案（等用户同意）

一屏内给出：

- **现状**：目录是否为空、已有文件。
- **项目形态**：语言、构建、测试、目录结构。
- **目标文档树**：用代码块列出将要生成的文件。
- **生成清单**：每个文件写什么，不写什么。
- **首版代码骨架**：只列最小可构建目标；不生成空模块。
- **不生成**：明确不做的模块、不写的空文档。
- **验证**：链接检查、构建、测试。
- **待你决定**：≤3 个，各带推荐。

**等用户明确同意后再写文件；“按推荐来”算同意。**

## 2. 生成文件

文档长度、拆分和索引规则见 `doc-system.md`。

按语言裁剪，默认生成：

```text
AGENTS.md
README.md
.gitignore
.clang-format              # C++
pytest.ini                 # Python
docs/README.md
docs/design/0.overview.md
docs/design/changes/README.md
docs/governance/coding-standards.md
docs/governance/commit-conventions.md
docs/governance/invariants.md
docs/governance/ai-workflow.md
docs/how-to/1.build-test-run.md
tests/test_docs_links.py   # 有 pytest 时
```

模板在 `references/templates/`：

| 模板 | 目标文件 |
| --- | --- |
| `templates/project/AGENTS.md` | `AGENTS.md` |
| `templates/project/README.md` | `README.md` |
| `templates/project/docs/README.md` | `docs/README.md` |
| `templates/project/docs/design/0.overview.md` | `docs/design/0.overview.md` |
| `templates/project/docs/design/changes/README.md` | `docs/design/changes/README.md` |
| `templates/project/docs/governance/coding-standards.md` | `docs/governance/coding-standards.md` |
| `templates/project/docs/governance/commit-conventions.md` | `docs/governance/commit-conventions.md` |
| `templates/project/docs/governance/invariants.md` | `docs/governance/invariants.md` |
| `templates/project/docs/governance/ai-workflow.md` | `docs/governance/ai-workflow.md` |
| `templates/project/docs/how-to/1.build-test-run.md` | `docs/how-to/1.build-test-run.md` |
| `templates/config/.clang-format` | `.clang-format` |
| `templates/config/pytest.ini` | `pytest.ini` |
| `templates/config/.gitignore` | `.gitignore` |
| `templates/config/test_docs_links.py` | `tests/test_docs_links.py` |

复制后必须替换占位符，删掉不适用的段落，不留空栏目。

## 3. 占位符

| 占位符 | 含义 | 示例 |
| --- | --- | --- |
| `<PROJECT>` | 项目显示名 | `LightRTF` |
| `<project>` | 仓库 / 包名 | `light_rtf` |
| `<PREFIX>` | 日志与宏前缀 | `LIGHT_RTF` |
| `<C++ 标准>` | 标准版本 | `C++20`（兼容旧工具链用 `C++17`） |
| `<模块>` | 模块名 | `engine` |
| `<构建命令>` | 构建命令 | `cmake -S . -B build && cmake --build build -j` |
| `<测试命令>` | 测试命令 | `ctest --test-dir build --output-on-failure` |

只索引实际存在的文档：模块文档创建后再加链接，不留占位死链。

替换后全局搜索 `<`（`grep -rn '<[A-Za-z]' docs AGENTS.md README.md`），确认占位符清零；模板代码块里的 `<...>` 示例除外。

## 4. 代码骨架

只有方案里被同意时才做：

- **C++**：CMakeLists + 一个 smoke test + 实际存在的模块目录；不生成的模块不建空目录。
- **Python**：`pyproject.toml` 或 `requirements.txt` + `pytest.ini` + 一个 smoke test。
- **混合**：先定主语言和绑定方式（如 pybind11），不预先写两套实现。
- 最小目标：能构建、能跑一个测试；不写业务占位实现，不虚构接口。

## 5. 验证与提交

- 有 pytest 时跑 `pytest tests/test_docs_links.py`；没有时用等价脚本检查死链和索引。
- 文档预算：Design 正文 ≤2500 字；每篇开头有状态块。
- 构建 + 测试：一条命令跑通。
- 提交：`chore: initialize project docs and skeleton`；首个功能另用 `feat(<scope>): ...`。

## 6. 之后

第一个需求走日常流程：六点约定 → `docs/design/changes/` 变更文档 → 实现 → 并入 Design。初始化时的 `0.overview` 只写已决定的架构和边界；没有实现的模块标“未定”，不要提前展开。
