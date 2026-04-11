# Step 014 — Aider 階段三：建立 .env 並配置模型 API

## 背景

在 Aider 已安裝、專案與 Git 狀態也確認正確之後，下一步建立 `.env`，讓 Aider 同時知道：

1. 本地 Ollama API 在哪裡
2. GitHub Copilot 的 OpenAI-compatible API base
3. 要使用哪個 Copilot OAuth token

## 本步策略

| 項目 | 內容 |
|---|---|
| 本地模型 API | `OLLAMA_API_BASE=http://127.0.0.1:11434` |
| 雲端模型 API | `OPENAI_API_BASE=https://api.githubcopilot.com` |
| Token 來源 | 直接從 `~/.config/github-copilot/apps.json` 讀取 |
| 安全原則 | 驗證時不印出 token 明文 |

## 狀態

等待使用者執行 `.env` 建立與驗證指令並回報結果。
