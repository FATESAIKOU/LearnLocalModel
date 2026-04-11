# Gemma 4 部署索引

本檔案只作為索引與目前狀態摘要；實際決策與步驟都分散在各自獨立檔案中。

## 命名規則

| 項目 | 規則 |
|---|---|
| 命名格式 | `{4位流水號}-{type}-{topic}.md` |
| 流水號規則 | 由小到大遞增，代表建立順序 |
| 編號原則 | **只新增，不重編，不插號** |
| 存放位置 | `./session/` |
| 目的 | 讓閱讀者只看檔名就能理解事件先後順序 |

## 已建立檔案

| 流水號 | 檔案 | 主題 |
|---|---|---|
| 0001 | `0001-step-environment-survey.md` | 環境調查結果與限制 |
| 0002 | `0002-decision-model-family-gemma4.md` | 為何從 Gemma 改為 Gemma 4 |
| 0003 | `0003-decision-model-size-e4b-first.md` | 為何先選 `gemma4:e4b`，之後再試 `gemma4:26b` |
| 0004 | `0004-decision-deployment-option-a-ollama.md` | 為何選方案 A：Ollama (Docker) |
| 0005 | `0005-step-runtime-validation.md` | Docker GPU runtime 驗證現況與卡點 |
| 0006 | `0006-decision-reporting-structure.md` | 為何改成每個決策一個檔案放在 `./session/` |
| 0007 | `0007-deployment-index.md` | 索引與目前狀態 |
| 0008 | `0008-decision-filename-sequencing.md` | 為何加入流水號命名系統 |
| 0009 | `0009-step-start-ollama-container.md` | 啟動 Ollama 容器與 API 驗證 |
| 0010 | `0010-step-pull-gemma4-e4b.md` | 下載 `gemma4:e4b` 並確認模型已註冊 |

## 目前狀態

| 階段 | 狀態 |
|---|---|
| 環境調查 | 完成 |
| 模型世代選擇 | 完成 |
| 模型大小選擇 | 完成 |
| 部署方案選擇 | 完成 |
| 報告規則調整 | 完成 |
| 檔名流水號規則 | 完成 |
| Docker GPU runtime 驗證 | 完成 |
| Ollama 安裝 | 完成 |
| 模型拉取 | 完成 |
| 推論測試 | 尚未開始 |
