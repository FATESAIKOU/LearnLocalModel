# Step 4-1 — Basic Inference Test

## Input

| Item | Value |
|---|---|
| Deployment option | A: Ollama (Docker) |
| Current status | `gemma4:e4b` is installed in Ollama |

## Process

Run the commands below in order.

```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:e4b",
    "prompt": "Reply with exactly one line: GEMMA4_E4B_OK",
    "stream": false
  }'

docker logs --tail 50 ollama
```

## Output

| Check item | Expected result |
|---|---|
| `curl http://localhost:11434/api/generate ...` | Returns JSON and the `response` field contains `GEMMA4_E4B_OK` |
| `docker logs --tail 50 ollama` | Shows the model request was handled without startup errors |

## Action

Paste the full command output back to the chat, then reply `REVIEWED`.
