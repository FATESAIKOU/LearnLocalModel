# Decision 012 — 明確標示 Aider 不是完整 read/write/bash 工具代理

## 背景

使用者發現 Aider 在要求「寫 ToDo Web App」時，會直接把內容輸出在畫面上，而不是像目前這個 CLI 一樣自動讀檔、改檔、跑 shell。這暴露出一個重要認知差異：Aider 不是完整的工具代理環境。

## 判讀

| 項目 | 結論 |
|---|---|
| Aider 是否有完整 read/write/bash 工具抽象 | 否 |
| Aider 是否能編輯檔案 | 是，但主要針對已加入聊天的檔案 |
| Aider 是否能執行 shell | 是，但以 `/run`、`/test` 這類指令為主，不等同完整 bash 工具 |
| 為何會只吐在畫面上 | 因為請求太抽象、缺少目標檔案上下文，或模型/模式不適合直接產生 edits |

## 結論

`Aider_Setup_Guide.md` 已補充：

1. Aider 的能力邊界
2. `/run`、`/test`、`/chat-mode` 的用途
3. 如何下 prompt 才更容易讓 Aider 直接改檔而不是只輸出文字
