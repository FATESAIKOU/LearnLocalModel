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

## 執行結果

| 項目 | 結果 |
|---|---|
| Token 來源 | `~/.config/github-copilot/apps.json` |
| `.env` 建立 | 完成 |
| `OLLAMA_API_BASE` | 已設定為 `http://127.0.0.1:11434` |
| `OPENAI_API_BASE` | 已設定為 `https://api.githubcopilot.com` |
| `OPENAI_API_KEY` | 已寫入 `.env`，且驗證時未明文輸出 |

## 結論

`.env` 已完成，Aider 階段三的四個子步驟均已完成，可進入最終說明文件產出。
