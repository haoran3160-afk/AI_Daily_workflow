# 开发与验证

## 原则

- 一次处理一个清楚的问题，使用小提交和显式暂存。
- 修改抓取、审核或写入行为时增加行为测试，不靠放宽 expected 获得全绿。
- 纯目录／导入整理与内容策略变更分开提交。
- 不在日常定时任务中开发，不把私有部署资产纳入公开仓库。

## 本地检查

在仓库根目录执行：

```powershell
.\.venv\Scripts\python.exe -m pytest tests
.\.venv\Scripts\python.exe -m ruff check src tests
.\.venv\Scripts\python.exe -m mypy src/pkm_workflow
git diff --check
```

测试构造合成上下文、来源和临时发布目录，适合离线验证；不代表每个真实来源当前可用，
也不代表内容已达到用户满意程度。真实内容验收在私有 runtime 中完成，不提交真实笔记。

## 目录约定

- 引擎代码放入 `src/pkm_workflow`，包内采用相对导入。
- `scripts` 保留薄命令入口，不另建模型执行器。
- `tests` 放自包含测试，不依赖仓库外的私人配置让公共 CI 通过。
- 首页解释产品，运行、配置和架构细节放入 `docs`。

`scripts/run_workflow.py` 及其 CLI 参数保持为仓库运行入口。目录整理后，原根目录内部模块
的导入路径为 `pkm_workflow.fetcher`、`pkm_workflow.source_registry` 和
`pkm_workflow.workflow_contracts`；直接引用旧根模块的开发脚本需更新。

## 现有个人部署

公开仓库与既有 MVP 运行 checkout 分开。本次目录／文档整理不切换正在使用的引擎路径、
定时任务或 Vault。今后同步新布局时应一起同步包内模块和调用方导入，不能只拷贝单个文件。
