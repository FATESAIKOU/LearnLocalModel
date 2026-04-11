# First-time container startup
```shell
docker volume create ollama
docker run -d \
  --name ollama \
  --restart unless-stopped \
  --gpus all \
  -p 11434:11434 \
  -v ollama:/root/.ollama \
  ollama/ollama:latest
```

# Pull Gemma 4 E4B
```shell
docker exec ollama ollama pull gemma4:e4b
```

# Start chat with Gemma 4 E4B
```shell
docker exec -it ollama ollama run gemma4:e4b
```

# One-shot prompt with Gemma 4 E4B
```shell
docker exec -it ollama ollama run gemma4:e4b "Please answer in Traditional Chinese. Use exactly 3 bullet points to explain what Docker, Ollama, and Gemma 4 do in this deployment."
```

# Pull Gemma 4 26B
```shell
docker exec ollama ollama pull gemma4:26b
```

# Start chat with Gemma 4 26B
```shell
docker exec -it ollama ollama run gemma4:26b
```

# One-shot prompt with Gemma 4 26B
```shell
docker exec -it ollama ollama run gemma4:26b "Please answer in Traditional Chinese. Use exactly 3 bullet points to explain what Docker, Ollama, and Gemma 4 do in this deployment."
```

# Check current service state
```shell
docker ps --filter name=ollama
curl http://localhost:11434/api/tags
docker exec ollama ollama list
```

# Show recent Ollama logs
```shell
docker logs --tail 100 ollama
```
