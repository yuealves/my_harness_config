# my_harness_config

个人常用 AI 编码工具的配置与 skills 仓库，默认用于 DeepSeek Harness（DSH），同时支持 Codex 和 Claude Code。

## 安装

先获取仓库：

```bash
git clone <this-repo-url> ~/Code/my_harness_config
cd ~/Code/my_harness_config
```

### DSH（默认）

```bash
chmod +x install-to-dsh.sh
./install-to-dsh.sh
```

默认安装到：

```text
~/.dsh/skills/<skill-name>
~/.dsh/AGENTS.md            # 全局中文偏好；已存在且不是本仓库的链接时跳过
```

默认使用 symlink，方便后续修改仓库内容后立即生效。可用选项：

```bash
./install-to-dsh.sh --dry-run
./install-to-dsh.sh --copy
DSH_HOME=/path/to/dsh ./install-to-dsh.sh
DSH_SKILLS_DIR=/path/to/skills ./install-to-dsh.sh
```

安装后重启 DSH 或开启新会话，让 skill 生效。

### Codex

把本仓库所有 skills 安装到 Codex：

```bash
chmod +x install-to-codex.sh
./install-to-codex.sh
```

默认安装到：

```text
~/.codex/skills/<skill-name>
```

默认使用 symlink。可用选项：

```bash
./install-to-codex.sh --dry-run
./install-to-codex.sh --copy
CODEX_HOME=/path/to/codex ./install-to-codex.sh
CODEX_SKILLS_DIR=/path/to/skills ./install-to-codex.sh
```

安装后重启 Codex 或开启新会话，让 skill 生效。

### Claude Code

把本仓库所有 skills 安装到 Claude Code：

```bash
chmod +x install-to-claude-code.sh
./install-to-claude-code.sh
```

默认安装到：

```text
~/.claude/skills/<skill-name>
```

## 当前 Skills

```text
docs-first
split-task
technical-plan
```

- `docs-first`：文档先行的开发约定：新项目初始化、既有项目改造、日常需求三种场景；按 `docs/design`、`docs/how-to`、`docs/governance` 维护文档，统一 C++/Python 代码规范与 commit 规范；改项目前先出方案等确认。
- `split-task`：用于总结或恢复当前任务，维护 `current_tasks.md`，拆分可验证子任务并同步 TodoWrite。
- `technical-plan`：用于大工程任务开工前调研现状、写技术方案文档、拆分实现/验证阶段，并等待用户确认后再实现。

## 历史

`setup.sh` 和 `opencode.json` 是早期 OpenCode 配置，保留但不再维护。
