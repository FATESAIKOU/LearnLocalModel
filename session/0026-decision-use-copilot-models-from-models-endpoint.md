# Decision 011 — Aider 的 Copilot 模型名稱以 /models 結果為準

## 背景

在 `Aider_Setup_Guide.md` 中曾把 `openai/gpt-5.4-mini` 寫成雲端模型範例，但實際執行後，Aider 回報該模型無法透過 `/chat/completions` 端點使用。

## 實際錯誤

```text
litellm.BadRequestError: OpenAIException - model "gpt-5.4-mini" is not accessible via the /chat/completions endpoint
```

## 判讀

| 項目 | 結論 |
|---|---|
| 問題性質 | README 中使用了不適用於 Copilot OpenAI-compatible chat endpoint 的模型名稱 |
| 根因 | 誤把其他工具可見的模型名，當成 Aider 可直接使用的模型名 |
| 修正原則 | Aider 可用模型一律以 `https://api.githubcopilot.com/models` 回傳結果為準 |

## 結論

README 已改為：

1. 用 `openai/gpt-4o` 作為保守範例
2. 明確要求先查 `/models`
3. 新增此錯誤的排錯章節
