# Step 015 — Aider 階段四：產出最終使用說明

## 背景

Aider 階段三已完成，因此依原規劃進入階段四，產出一份可交接、可重建、可日常使用的完整說明文件。

## 產出檔案

| 項目 | 內容 |
|---|---|
| 檔名 | `Aider_Setup_Guide.md` |
| 目的 | 提供從零配置、日常使用、熱切換與排錯說明 |

## 文件內容

`Aider_Setup_Guide.md` 已包含：

1. 從零開始的配置步驟
2. `aider-chat` 安裝
3. `.env` 建立與載入
4. 本地 Ollama 啟動方式
5. GitHub Copilot OpenAI-compatible 用法
6. `/add`、`/model` 等日常指令
7. 本地與雲端模型的熱切換示例
8. 常見授權與連線排錯

## 補充修正

後續驗證發現原文件中的 `openai/gpt-5.4-mini` 範例不可直接透過 Copilot 的 `/chat/completions` 端點使用，因此已改為 `openai/gpt-4o`，並新增「先查 `/models` 再選模型」的說明與對應排錯。

## 結論

階段四已完成，且最終說明文件已依實際執行結果修正。
