# Step 005 — 下載 Gemma 4 E4B 模型

## Input

| 項目 | 內容 |
|---|---|
| 服務狀態 | Ollama 容器已啟動 |
| 目標模型 | `gemma4:e4b` |

## Process

要求使用者在容器內拉取模型，並用 CLI 與 API 雙重確認模型已註冊。

## 已執行指令

```bash
docker exec ollama ollama pull gemma4:e4b

docker exec ollama ollama list

curl http://localhost:11434/api/tags
```

## Output

| 項目 | 結果 |
|---|---|
| Pull 狀態 | 成功 |
| 模型名稱 | `gemma4:e4b` |
| 模型大小 | 9.6 GB |
| 格式 | GGUF |
| 量化 | `Q4_K_M` |
| API 狀態 | 可透過 `/api/tags` 查到模型 |

## 關鍵輸出

```text
pulling 4c27e0f5b5ad: 100% 9.6 GB
verifying sha256 digest
writing manifest
success

NAME          ID              SIZE
gemma4:e4b    c6eb396dbd59    9.6 GB
```

## 結論

`gemma4:e4b` 已成功安裝到 Ollama，可進入實際推論測試。
