# 配置与数据边界

此页是当前部署参考，不是新的配置框架。路径仍在代码中声明；当前没有一个通用
`--config` 参数或环境变量可以替代所有路径设置。

## 外部文件

| 文件 | 作用 | 验证入口 |
| --- | --- | --- |
| `Source-Manifest-v7.5.json` | 来源、分层、抓取节奏与访问资格 | [source_catalog.py](../src/pkm_workflow/source_catalog.py) |
| `UserContextContract-v7.5.json` | 明确批准的兴趣、项目与已读背景 | [user_context_v75.py](../src/pkm_workflow/user_context_v75.py) |
| `Knowledge-Anchors-v7.5.json` | 精确允许访问的知识锚点，可为空 | [user_context_v75.py](../src/pkm_workflow/user_context_v75.py) |

示意文件说明见 [examples](../examples/README.md)。实际文件应放在仓库外，不提交到 Git。
来源“已收录”不等于“适配器已激活”；以实际状态与可读取的免费正文为准。

## 路径与批准上下文

更换个人部署时，一起检查以下声明：

- `source_catalog.APPROVED_SOURCE_MANIFEST_PATH`。
- `user_context_v75.PRIVATE_CONTEXT_PATH`、`PRIVATE_ANCHORS_PATH`、`VAULT_ROOT`。
- `user_context_v75.APPROVED_USER_CONTEXT_V75_HASH`。
- `ai_daily_luna.RUNTIME`。
- `ai_daily_production.VAULT_DAILY_DIR` 与 `PRODUCTION_LOCK_PATH`。

批准 hash 对规范化后的完整上下文 JSON 计算，相关函数位于上下文加载器。
明确检查并批准配置后才更新它；它检测配置变化，不是账户密码或加密认证。

## 输出与状态

最终笔记写入批准的 `30-Daily`。草稿、审核、证据和报告留在外部 runtime；
正式发布记录用于去重及周报汇总。不要只移动 Markdown 而丢弃与其绑定的运行记录。

日／周发布均有同名保护和已有文件校验。外部编辑导致记录不一致时，流程可能停止，
而不是自动覆盖用户修改。

## 模型与隐私

当前生成和审核固定为 `gpt-5.6-luna / medium`，模型在 Codex 会话中运行。
项目不读取 `.env` 来调用 DeepSeek 或独立 OpenAI API，也不自动充值。

选中的证据和批准上下文会传给 Codex，本地存储不等于全程离线。
不要配置与简报无关的私密材料。排查问题时只分享脱敏错误码与最小复现，
不上传原笔记、完整上下文、访问凭据或 runtime 目录。
