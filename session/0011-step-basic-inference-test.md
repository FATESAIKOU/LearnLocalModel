# Step 006 — 基本推論測試通過

## Input

| 項目 | 內容 |
|---|---|
| 服務狀態 | Ollama 容器運作中 |
| 模型 | `gemma4:e4b` |
| 測試目標 | 確認模型可接收 prompt 並正確輸出固定字串 |

## Process

要求使用者透過 Ollama HTTP API 發送最小化測試請求，並查看容器日誌以確認模型載入與推論流程正常。

## 已執行指令

```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:e4b",
    "prompt": "Reply with exactly one line: GEMMA4_E4B_OK",
    "stream": false
  }'

docker logs --tail 50 ollama
```

## Output

| 項目 | 結果 |
|---|---|
| API 回應 | 成功 |
| 測試輸出 | `GEMMA4_E4B_OK` |
| 推論模式 | 非串流 (`stream: false`) |
| 模型載入 | 成功 |
| GPU 使用 | 已啟用，42/43 layers offloaded to GPU |
| 執行結果 | 可進入後續更完整測試 |

## 關鍵輸出

```text
{"model":"gemma4:e4b","response":"GEMMA4_E4B_OK","done":true,"done_reason":"stop"}
```

```text
offloading 42 repeating layers to GPU
offloading output layer to CPU
offloaded 42/43 layers to GPU
[GIN] 2026/04/11 - 04:03:24 | 200 |         1m32s |      172.17.0.1 | POST     "/api/generate"
```

## 判讀

| 檢查項目 | 結論 |
|---|---|
| HTTP API 是否可用 | 是 |
| 模型是否成功載入 | 是 |
| GPU acceleration 是否生效 | 是 |
| 是否已具備基本可用性 | 是 |

## 結論

`gemma4:e4b` 已在此主機上成功完成一次實際推論，代表 Gemma 4 本地部署已可正常接收 prompt 並產生回應。
