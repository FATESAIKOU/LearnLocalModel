# Step 4-2 — Practical Prompt Test

## Input

| Item | Value |
|---|---|
| Deployment option | A: Ollama (Docker) |
| Current status | Basic inference test passed |

## Process

Run the commands below in order.

```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:e4b",
    "prompt": "Please answer in Traditional Chinese. Explain in exactly 3 bullet points what Docker, Ollama, and Gemma 4 each do in this deployment.",
    "stream": false
  }'

docker logs --tail 50 ollama
```

## Output

| Check item | Expected result |
|---|---|
| `curl http://localhost:11434/api/generate ...` | Returns JSON and the `response` field contains a meaningful Traditional Chinese answer |
| `docker logs --tail 50 ollama` | Shows the model request was handled without startup errors |

## Action

Paste the full command output back to the chat, then reply `REVIEWED`.
