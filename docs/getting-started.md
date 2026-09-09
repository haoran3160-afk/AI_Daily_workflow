# 本地上手指南

目标是先确认代码可运行，再配置个人部署。此指南的测试步骤不会写入真实 Vault。

## 1. 准备环境

- Windows。当前文件锁使用 Windows 接口，尚未声明跨平台支持。
- Python 3.12 与 Git。
- Codex 桌面应用以及可用的模型／任务额度。
- 本地 Obsidian Vault。
- GitHub CLI，供项目元数据和 README 抓取使用。

## 2. 安装并验证

```powershell
git clone https://github.com/haoran3160-afk/AI_Daily_workflow.git
cd AI_Daily_workflow
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest tests
.\.venv\Scripts\python.exe scripts/run_workflow.py --help
```

测试使用临时目录和合成数据，不需要你的私有配置，不会写入真实 Vault。

## 3. 配置个人部署

当前版本仍保留原部署的外部路径和批准上下文摘要。换到另一台机器时，需要按
[配置参考](configuration.md) 准备完整配置，并调整列出的路径与上下文 hash。
不要直接复制他人的批准 hash，也不要把示意 JSON 当作可运行配置。

这一步是本地部署工作，不在每日自动任务中执行。仓库不会自动安装一个定时任务。

## 4. 先完成一次预览

配置完成后，通过 Codex 按运行手册执行：

```powershell
.\.venv\Scripts\python.exe scripts/run_workflow.py --workflow ai --mode shadow --stage prepare
```

`GENERATOR_READY` 表示候选包已准备好，**并不表示日报已经生成**。
Codex 中的生成角色写出草稿后，再执行 `review`，交由新上下文的独立 Luna Reviewer 审核，
最后运行 `finalize`。使用各阶段返回的 run ID 和路径，Python 不会自行调用模型。

详细步骤见 [运行手册](ai-daily-luna.md)。覆盖不足或审核失败时，先处理原因，不制造内容通过。

## 5. 设置定时运行

预览通过后，在 Codex 当前本地项目中创建一个每天 08:00 的自动任务，固定使用引擎和 Python
的绝对路径，并让任务完整执行运行手册。默认周一至周六生成日报，周日生成周报，不需要两个任务。

正式发布使用 `--mode production`，最终阶段必须加 `--confirm-vault-write`。
同名笔记存在时跳过；不要通过改日期或另建 run 绕过保护。

本地任务依赖电脑开机、应用运行和项目目录可访问，详见
[官方计划任务说明](https://learn.chatgpt.com/docs/automations?surface=app)。
