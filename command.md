# Step 3-2 — Start Ollama Container

## Input

| Item | Value |
|---|---|
| Deployment option | A: Ollama (Docker) |
| Current status | Docker GPU runtime verified |

## Process

Run the commands below in order.

```bash
docker volume create ollama

docker run -d \
  --name ollama \
  --restart unless-stopped \
  --gpus all \
  -p 11434:11434 \
  -v ollama:/root/.ollama \
  ollama/ollama:latest

docker ps --filter name=ollama

curl http://localhost:11434/api/tags
```

If the last command does not return JSON yet, run:

```bash
docker logs --tail 50 ollama
```

## Output

| Check item | Expected result |
|---|---|
| `docker run -d ...` | Returns a container ID |
| `docker ps --filter name=ollama` | Shows `ollama` in `Up` status |
| `curl http://localhost:11434/api/tags` | Returns JSON with a `models` field |
| `docker logs --tail 50 ollama` | Shows service startup logs |

## Action

Paste the full command output back to the chat, then reply `REVIEWED`.
