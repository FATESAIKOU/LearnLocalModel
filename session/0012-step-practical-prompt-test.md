# Step 007 — 實際問答測試通過

## Input

| 項目 | 內容 |
|---|---|
| 模型 | `gemma4:e4b` |
| 測試方式 | 透過 Ollama HTTP API 發送自然語言問題 |
| 測試目標 | 驗證模型不只會固定字串回應，也能完成一般問答 |

## Process

要求使用者送出一個實際 prompt，內容指定模型以繁體中文回答，並用 3 個 bullet points 說明 Docker、Ollama、Gemma 4 在本次部署中的角色；同時查看容器日誌確認請求被正常處理。

## 已執行指令

```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:e4b",
    "prompt": "Please answer in Traditional Chinese. Explain in exactly 3 bullet points what Docker, Ollama, and Gemma 4 each do in this deployment.",
    "stream": false
  }'

docker logs --tail 50 ollama
```

## Output

| 項目 | 結果 |
|---|---|
| API 回應 | 成功 |
| 回應語言 | 繁體中文 |
| 回應型態 | 3 個 bullet points |
| 內容品質 | 能正確描述 Docker、Ollama、Gemma 4 的分工 |
| HTTP 狀態 | 200 |
| 本次推論耗時 | 約 29.3 秒 |

## 關鍵輸出

```text
{"model":"gemma4:e4b","response":"以下是三個核心元件各自在部署中所扮演的角色： ... ","done":true,"done_reason":"stop"}
```

```text
[GIN] 2026/04/11 - 04:06:03 | 200 | 29.299244486s | 172.17.0.1 | POST "/api/generate"
```

## 判讀

| 檢查項目 | 結論 |
|---|---|
| 模型是否能理解一般 prompt | 是 |
| 模型是否能依指示使用繁體中文 | 是 |
| 模型是否能輸出結構化回答 | 是 |
| API 與服務端是否穩定 | 是 |

## 補充觀察

| 項目 | 觀察 |
|---|---|
| 首次請求 | 約 1 分 32 秒，主要花在載入模型 |
| 後續請求 | 約 29 秒，明顯快於冷啟動 |
| GPU offload | 仍維持 42/43 layers offloaded to GPU |

## 結論

本機部署的 `gemma4:e4b` 已不只通過最小驗證，也通過一次實際問答測試；至此可判定此部署已具備可用的本地推論能力。
