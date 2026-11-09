# AGENTS.md

> AI agent 进入本仓库的第一入口。人类读者请从 README.md 开始。

## 必读顺序

1. 本文件。
2. [`docs/README.md`](docs/README.md)：文档地图和按意图的阅读路径。
3. [`docs/design/0.overview.md`](docs/design/0.overview.md)：目标、架构、依赖红线。
4. `docs/governance/` 全部：代码规范、commit 规范、正确性不变量、AI 协作与文档规约。
5. 你要修改的模块的 `docs/design/<编号>.<模块>.md`。

## 项目一句话

<PROJECT>：<一句话说明解决什么问题、主要能力是什么>。

## 协作约定（每次对话）

- 除一句话能说清的小改动，先用 2–3 句复述需求，再给六点草案（目的 / 支持 / 排除 / 不变量 / 失败 / 验收）；用户确认后再改文件。
- 只问影响业务、正确性或维护成本的问题，每轮 ≤3 个，给选项、后果和推荐。
- 改造项目前先给方案并等用户同意；范围变化只说“原约定 → 新发现 → 推荐调整”。
- 交付一屏：行为变化、实际验证、剩余限制、改了哪篇文档、待决事项。

完整规则见 `docs/governance/ai-workflow.md`。新会话先读它，不要依赖外部 skill。

## 红线（违反任何一条都必须有用户明确拍板）

1. **Commit message 一律用英文**：Conventional Commits `<type>(<scope>): <summary>`，summary 和正文都用英文；禁止中文提交信息。详见 `docs/governance/commit-conventions.md`。
2. **依赖单向**：<模块依赖方向，例如 base ← market ← factors ← engine ← app>；禁止反向 include。
3. **正确性不变量**：见 `docs/governance/invariants.md`，违反即视为回归。
4. **热路径零日志**：只允许 `<PREFIX>_LOG_*` / `<PREFIX>_DEBUG_LOG` 宏，编译期裁剪；禁止裸 `std::cerr` / `printf` / 直接调用日志库。
5. **不引入新第三方依赖**（当前例外：<无 / 依赖名>）。
6. **<项目特有红线>**：<工具链、线上操作、测试链接、数据格式等>。

## 会话 IO 纪律

预判输出超过几百行的命令，先重定向到文件，再用 `tail` / `grep` 取摘要；不要在会话里直接打印大段输出。

```bash
mkdir -p /tmp/<project>_logs
<大输出命令> > /tmp/<project>_logs/run.log 2>&1
echo "exit=$?"
tail -n 40 /tmp/<project>_logs/run.log
```

## 验证命令

```bash
<构建命令>
<测试命令>
```

## 常用路径

- 模块设计：`docs/design/`
- 操作手册：`docs/how-to/`
- 规范：`docs/governance/`
- 变更记录：`docs/design/changes/`
