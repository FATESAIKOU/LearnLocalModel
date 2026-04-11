# Decision 009 — command.md 先放 docker run 再放 docker exec

## 背景

使用者指出對 Docker 的預期流程是先 `docker run` 啟動 container，之後才 `docker exec` 進入既有 container。這個理解是正確的，而先前 `command.md` 把 `docker exec` 放在前面，容易造成誤解。

## Input

| 項目 | 內容 |
|---|---|
| 使用者回饋 | 以為應該先 `docker run container` 再 `docker exec` |
| 目前問題 | `command.md` 以已啟動 container 的情境為主，但沒有先交代 lifecycle |

## DA 表

| 欄位 | 內容 |
|---|---|
| 技術/決策的採用前提 | Docker 的基本操作流程需要與使用者心智模型一致 |
| 採用目的(效果) | 讓 `command.md` 從首次部署到後續 chat 都符合正確順序 |
| 結果影響內容 | 檔案最前面改回 `docker run -d ...`，後續再接 `docker exec ...` |
| 結果影響範圍 | 後續所有使用 `command.md` 的操作 |
| 採用成本 | 低 |

## 結論

`command.md` 已改為：

1. 先建立 volume
2. 再 `docker run -d` 啟動 `ollama` container
3. 之後才用 `docker exec` 做 pull、chat、單次問答與狀態檢查

這樣同時符合 Docker 正常流程與使用者直覺。
