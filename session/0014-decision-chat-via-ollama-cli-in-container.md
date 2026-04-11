# Decision 007 — 互動 chat 採用容器內 Ollama CLI

## 背景

使用者希望能直接開一個 chat，最好把某種 CLI 接到目前已啟動的 Ollama container。候選方向包含 GitHub Copilot CLI 或其他可用 CLI。

## Input

| 項目 | 內容 |
|---|---|
| 目前服務 | Ollama container 已啟動 |
| 已安裝模型 | `gemma4:e4b` |
| 使用者需求 | 能直接 chat，且最好能切換到 `gemma4:26b` |

## DA 表

| 欄位 | 內容 |
|---|---|
| 技術/決策的採用前提 | 需要最少額外安裝、最低整合成本、立即可用 |
| 採用目的(效果) | 讓使用者直接在終端機與本地模型互動 |
| 結果影響內容 | 優先使用容器內建的 `ollama run` 作為 chat CLI |
| 結果影響範圍 | 後續所有本地互動測試與手動使用方式 |
| 採用成本 | 最低 |

## 判斷

| 選項 | 結論 |
|---|---|
| Copilot CLI 直接改接 Ollama | 目前文件未提供這種模型 backend 切換設定，不採用 |
| 直接使用容器內 Ollama CLI | 可立即使用，採用 |

## 結論

`command.md` 已改為直接提供以下互動 chat 指令：

1. `docker exec -it ollama ollama run gemma4:e4b`
2. `docker exec -it ollama ollama run gemma4:26b`

這樣不需要額外安裝新工具，就能直接連到現有 Ollama container 開始聊天。
