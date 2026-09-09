# 架构与模块分工

项目保留一个 Python 包、一个命令入口和一条生成／审核链路，没有独立服务、数据库或任务队列。

| 职责 | 模块 |
| --- | --- |
| 日／周节奏 | `cadence.py` |
| 日报来源筛选 | `module_collection.py`、`source_catalog.py`、`v75_collection.py` |
| RSS、正文与来源记录 | `fetcher.py`、`source_registry.py`、`workflow_contracts.py` |
| 原论文取材 | `paper_collection.py` |
| 周报历史取材 | `weekly_collection.py` |
| 用户上下文与证据包 | `user_context_v75.py`、`daily_content.py` |
| 生成契约与 Markdown 渲染 | `daily_brief.py` |
| 三阶段协调与审核绑定 | `ai_daily_luna.py` |
| 正式发布与恢复 | `ai_daily_production.py` |
| 命令入口 | `cli.py`、`scripts/run_workflow.py` |

引擎模块位于 [src/pkm_workflow](../src/pkm_workflow)，命令脚本位于 [scripts](../scripts)。

## 三种责任

**Codex** 启动流程、生成结构化草稿，并委派独立审核角色。审核者不继承生成聊天历史。

**Python** 准备输入，校验结构与来源绑定，渲染 Markdown，处理同名保护和发布记录。
它不启动内容模型，也不发布未通过审核的材料。

**Obsidian** 保存和阅读最终 Markdown。工作流不修改 `.obsidian`，不自动安装插件。

## 共用底座

日报从轮到的两个模块抓取候选，周报读取本周已验证的日报材料。各来源的日期、署名和解释
性质保持分开，防止把旧判断当新事实。两者随后进入同一生成、审核、渲染与发布链路。

具体状态、预算和修复边界以 [运行手册](ai-daily-luna.md) 为准。
