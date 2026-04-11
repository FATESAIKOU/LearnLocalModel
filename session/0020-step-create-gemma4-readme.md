# Step 011 — 建立 Gemma 4 安裝與啟動 README

## 背景

使用者要求新增一份 `SETUP-GEMMA4-README.md`，將先前已完成的 Gemma 4 部署流程整理成可直接閱讀的 SOP，內容需涵蓋 `gemma4:e4b` 與 `gemma4:26b` 的安裝與啟動方式。後續又補充要求：不想每次都重新下載模型，因此 README 需改為先 build 一個已預載模型的自訂 image。

## Input

| 項目 | 內容 |
|---|---|
| 目標檔名 | `SETUP-GEMMA4-README.md` |
| 文件目的 | 從零開始說明 Gemma 4 環境如何安裝、啟動、驗證與切換模型 |
| 涵蓋模型 | `gemma4:e4b`, `gemma4:26b` |

## 內容範圍

README 已整理以下內容：

1. 目標環境規格
2. 模型策略
3. NVIDIA Container Toolkit 安裝
4. 用 stdin Dockerfile build 預載模型的自訂 image
5. 用自訂 image 啟動 Ollama container
6. `gemma4:e4b` chat、API 測試
7. `gemma4:26b` chat、單次問答
8. 日常操作與故障檢查
9. 最短重建路徑

## 結論

`SETUP-GEMMA4-README.md` 已更新於專案根目錄，可作為後續 Gemma 4 環境重建與交接文件，並避免每次重建都重新下載模型。
