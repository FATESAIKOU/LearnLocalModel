# Step 009 — Aider 階段二：依賴、安裝與驗證方式定義

## 背景

在正式安裝 Aider 前，先定義這套雙引擎架構所需的依賴、核心組件、安裝方式與驗證方式，讓後續階段三可以照清單逐步執行。

## Input

| 項目 | 內容 |
|---|---|
| 架構 | 本地 Ollama + 雲端 GitHub Copilot + Aider |
| 配置原則 | 盡量使用原生 Aider 設定 |
| Token 策略 | GitHub Copilot token 在階段三一起配置 |

## 依賴清單

| 類別 | 組件 | 用途 | 安裝方式 | 驗證方式 |
|---|---|---|---|---|
| 系統基礎 | `python3` | 執行 Aider | apt | `python3 --version` |
| 系統基礎 | `python3-pip` | 安裝 Python 套件 | apt | `python3 -m pip --version` |
| 系統基礎 | `git` | 提供 Aider Git 工作流 | apt | `git --version` |
| 核心工具 | `aider-chat` | Aider 主程式 | pip | `aider --version` |
| 本地模型 | Ollama API | 提供本地模型服務 | 既有 Docker container | `curl http://localhost:11434/api/tags` |
| 專案設定 | `.env` | 集中管理模型與 token 設定 | 手動建立 | `cat .env` |

## 階段二結論

後續階段三將依序執行：

1. 安裝與確認系統基礎套件
2. 安裝 `aider-chat`
3. 進入專案目錄並確認 Git 狀態
4. 建立 `.env` 並配置 Ollama 與 GitHub Copilot 相關變數
5. 驗證 Aider 是否能打到本地與雲端模型

## 狀態

階段二已完成，等待進入階段三實作。
