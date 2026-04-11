# Decision 010 — 改用預載模型的自訂 Ollama image

## 背景

使用者不希望每次重建環境時都重新下載 `gemma4:e4b` 與 `gemma4:26b`。因此原本 README 中「啟動 container 後再 pull 模型」的流程，需要改為「先 build 一個已內含模型的 image，之後都用那個 image 啟動」。

## Input

| 項目 | 內容 |
|---|---|
| 使用者要求 1 | 不想每次都下載 e4b 與 26b |
| 使用者要求 2 | README 要補 build 指令 |
| 使用者要求 3 | Dockerfile 不另外建檔，直接從 stdin 傳進 `docker build` |

## DA 表

| 欄位 | 內容 |
|---|---|
| 技術/決策的採用前提 | 已接受 image 體積變大，換取部署時不必重新拉模型 |
| 採用目的(效果) | 把兩個 Gemma 4 模型烘進 image，後續直接啟動即可 |
| 結果影響內容 | README 改為先 `docker build` 自訂 image，再 `docker run` 該 image |
| 結果影響範圍 | 後續所有 Gemma 4 重建、交接與日常啟動流程 |
| 採用成本 | 中 |

## 關鍵注意事項

1. 啟動時不能再把空 volume 掛到 `/root/.ollama`，否則會遮住 image 內的預載模型。
2. 這個 image 會很大，但可避免每次重建時再次下載模型。

## 結論

`SETUP-GEMMA4-README.md` 已更新為：

1. 用 stdin Dockerfile 執行 `docker build`
2. build 出 `local/ollama-gemma4:latest`
3. 後續一律用該 image 啟動 `ollama` container
