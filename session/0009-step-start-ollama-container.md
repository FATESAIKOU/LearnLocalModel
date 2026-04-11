# Step 004 — 啟動 Ollama 容器

## Input

| 項目 | 內容 |
|---|---|
| 已選方案 | A：Ollama (Docker) |
| 前置條件 | Docker GPU runtime 驗證完成 |

## Process

要求使用者建立持久 volume、啟動 `ollama/ollama:latest` 容器，並檢查容器狀態與 API 是否可連線。

## 已執行指令

```bash
docker volume create ollama

docker run -d \
  --name ollama \
  --restart unless-stopped \
  --gpus all \
  -p 11434:11434 \
  -v ollama:/root/.ollama \
  ollama/ollama:latest

docker ps --filter name=ollama

curl http://localhost:11434/api/tags
```

## Output

| 項目 | 結果 |
|---|---|
| Docker volume | `ollama` 已建立 |
| Container image | `ollama/ollama:latest` 已成功拉取 |
| Container status | `ollama` 為 `Up` 狀態 |
| API endpoint | `http://localhost:11434/api/tags` 可回應 |
| 模型列表 | 目前為空，表示服務正常但尚未下載模型 |

## 關鍵輸出

```text
CONTAINER ID   IMAGE                  COMMAND               STATUS   PORTS
adf547e9164a   ollama/ollama:latest   "/bin/ollama serve"   Up       0.0.0.0:11434->11434/tcp

{"models":[]}
```

## 結論

Ollama server 已成功啟動，系統已準備好下載 `gemma4:e4b`。
