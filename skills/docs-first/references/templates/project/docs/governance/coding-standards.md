# 代码规范

格式部分由 `.clang-format`（C++）和项目的格式化配置（Python）固化；本文记录必须人工遵守的部分。存量代码可能未完全符合：新增和改动的代码按本文执行，重构到时再统一，不做全库重写。

## C++

### 格式化

- 提交前 `clang-format -i <file>`；配置见根目录 `.clang-format`。
- 列宽 100，缩进 2 空格，指针左对齐；include 分组：本模块 → 项目内 → 系统/第三方。

### 命名

| 实体 | 风格 | 示例 |
| --- | --- | --- |
| 类型 / 类 / 结构体 | CamelCase | `SymbolWorker`、`IFactorFamily` |
| 函数 / 变量 | snake_case | `close_window`、`cutoff_nano` |
| 成员变量 | 尾下划线 | `states_` |
| 常量 | kCamelCase | `kMaxBatchSize` |
| 宏 | 全大写下划线，统一前缀 | `<PREFIX>_LOG_INFO` |
| 命名空间 | snake_case | `<project>::<module>` |

### 文件组织

- 头文件在 `include/<project>/<module>/`，实现在 `src/<module>/`，镜像组织。
- include 用完整路径：`#include "<project>/<module>/<file>.h"`。
- 头文件必须自包含，用 `#pragma once`；禁止在头文件里 `using namespace`。

### 硬规则

1. **热路径零日志**：只允许 `<PREFIX>_LOG_*` / `<PREFIX>_DEBUG_LOG` 宏；禁止裸 `std::cerr` / `printf` / 直接调日志库。
2. **日志禁止运行时 if 分支**：不允许 `if (debug_) LOG(...)`；裁剪只在编译期发生。
3. **性能插桩**只允许 `PERF_*` 宏（编译开关控制），禁止手写计时代码散在业务里。
4. **注释一律用英文**（C++/Python/shell/CMake）；写“为什么”和不变量，不写“是什么”的复读。用户可见字符串优先英文。
5. **依赖单向**：见 `docs/design/0.overview.md`；禁止反向 include。
6. **测试链接**：<纯逻辑测试用 header-only boost.test；链 Arrow 等重依赖的测试用动态链接变体；按项目实际填写，写错会在特定镜像下崩>。
7. **C++ 标准**：<默认 C++20；需要兼容旧 gcc/boost 时用 C++17>。

## Python

- PEP 8，4 空格缩进；行宽 100，或项目 ruff / black 的配置优先。
- 模块、函数、变量用 snake_case；类用 CamelCase；模块常量 UPPER_SNAKE；私有名前缀 `_`。
- 公开函数和数据结构写类型注解，用 `list[str]`、`X | None` 这类现代写法。
- docstring 用英文；写参数、返回、异常和“为什么”，不写复读式注释。
- 导入顺序：标准库 → 第三方 → 本项目；同包内优先相对导入。
- 错误显式抛出（`ValueError` 或自定义异常），消息用英文；不静默吞异常。
- 测试用 pytest，按 `unit` / `reference` / `e2e_*` 标记；默认只跑 `unit`。
- 不用 `print` 调试；用 logging 或测试断言。
