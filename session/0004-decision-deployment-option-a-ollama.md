# Decision 003 — 採用方案 A：Ollama (Docker)

## 背景

已確定要部署 Gemma 4，且優先型號為 `gemma4:e4b`。接下來需在三種方案中選擇實際部署方式。

## Input

| 項目 | 內容 |
|---|---|
| OS | Ubuntu 24.04.3 LTS |
| Docker | 已安裝 |
| CUDA Toolkit | 未安裝 |
| 目標 | 先快速跑起來 |

## DA 表

| 欄位 | A：Ollama (Docker) | B：llama.cpp (Native) | C：vLLM (Docker) |
|---|---|---|---|
| 技術/決策的採用前提 | Docker 可用 | 需裝 CUDA Toolkit 與編譯工具 | 需更完整的 GPU serving 設定 |
| 採用目的(效果) | 以最低成本啟動本地推論 | 取得更細緻的底層控制 | 建立偏服務化的推論 API |
| 結果影響內容 | 模型管理與 offload 較自動化 | 需手動管理模型與參數 | 設定與相容性處理較複雜 |
| 結果影響範圍 | 開發、測試、單機推論 | 單機推論、效能研究 | 多請求服務 |
| 採用成本 | 低 | 中 | 高 |

## 結論

使用者選擇 **方案 A：Ollama (Docker)**，因為它最符合「先跑起來」的目標，且目前環境已具備 Docker。
