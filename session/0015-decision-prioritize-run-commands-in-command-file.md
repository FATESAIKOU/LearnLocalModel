# Decision 008 — 把 `ollama run` 指令移到 command.md 最前面

## 背景

雖然 `command.md` 內已經有 `docker exec -it ollama ollama run ...` 指令，但它排在檢查與 pull 指令後面，使用者閱讀時不容易第一眼看到，因此回饋「沒有 run 指令」。

## Input

| 項目 | 內容 |
|---|---|
| 使用者回饋 | `NG 沒有 run 指令噎` |
| 目前問題 | `run` 指令存在，但不夠顯眼 |

## DA 表

| 欄位 | 內容 |
|---|---|
| 技術/決策的採用前提 | 使用者主要把 `command.md` 當作直接複製執行清單 |
| 採用目的(效果) | 讓「開 chat」成為最先看到、最先可執行的命令 |
| 結果影響內容 | `command.md` 重新排序，先放 `ollama run`，再放 pull、檢查、logs |
| 結果影響範圍 | 後續互動 chat 操作方式 |
| 採用成本 | 低 |

## 結論

`command.md` 已重新排序：

1. 最前面是 `gemma4:e4b` / `gemma4:26b` 的 `run` 指令
2. 其次是一次性問答
3. 最後才是 pull / state / logs

這樣更符合使用者想直接開 chat 的使用方式。
