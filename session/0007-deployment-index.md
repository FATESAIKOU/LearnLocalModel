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
| 0011 | `0011-step-basic-inference-test.md` | 基本推論測試與 GPU offload 結果 |
| 0012 | `0012-step-practical-prompt-test.md` | 實際問答測試與回應品質確認 |
| 0013 | `0013-decision-command-file-pure-commands-and-model-switch.md` | `command.md` 改成純指令串並支援 `gemma4:26b` |
| 0014 | `0014-decision-chat-via-ollama-cli-in-container.md` | 採用容器內 Ollama CLI 作為互動 chat 入口 |
| 0015 | `0015-decision-prioritize-run-commands-in-command-file.md` | 把 `ollama run` 指令移到 `command.md` 最前面 |
| 0016 | `0016-decision-command-file-start-with-docker-run.md` | `command.md` 改回先 `docker run` 再 `docker exec` |
| 0017 | `0017-step-aider-phase1-goals-and-constraints.md` | Aider 階段一：目標、架構與每階段 session 規則 |
| 0018 | `0018-step-aider-phase2-dependencies-and-validation.md` | Aider 階段二：依賴與驗證清單 |
| 0019 | `0019-step-aider-phase3-system-bootstrap.md` | Aider 階段三：系統基礎環境安裝 |
| 0020 | `0020-step-create-gemma4-readme.md` | 建立 Gemma 4 安裝與啟動 README |
| 0021 | `0021-decision-build-preloaded-ollama-image.md` | 改用預載 `e4b` 與 `26b` 的自訂 Ollama image |

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
| 推論測試 | 完成 |
