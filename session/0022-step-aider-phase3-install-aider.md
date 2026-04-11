# Step 012 — Aider 階段三：安裝 aider-chat

## 背景

在系統基礎套件確認可用後，下一步安裝 `aider-chat`，並驗證 Aider 指令是否可正常執行。

## 本步目標

| 項目 | 內容 |
|---|---|
| 安裝套件 | `aider-chat` |
| 安裝方式 | `python3 -m pip install --user -U aider-chat` |
| 驗證方式 | `aider --version` 或 `~/.local/bin/aider --version` |

## 執行結果

| 項目 | 結果 |
|---|---|
| `aider-chat` 安裝 | 成功 |
| 版本 | `0.86.x` |
| 安裝位置 | 使用者層級 pip (`--user`) |
| pip 相依性警告 | 有，但不阻塞本步 |

## 補充觀察

安裝過程中出現多個既有 Python 套件的 dependency conflict 警告，代表目前使用者層級 Python 環境內已有其他套件，版本需求與 Aider 新裝依賴不同。此情況**不影響 Aider 本身啟動**，但後續若同一個 Python 環境還要跑其他工具，可能需要改用虛擬環境隔離。

## 結論

`aider-chat` 已成功安裝，可進入下一步確認目標專案與 Git 狀態。
