# Check current service state
docker ps --filter name=ollama
curl http://localhost:11434/api/tags
docker exec ollama ollama list

# Ensure Gemma 4 E4B is present
docker exec ollama ollama pull gemma4:e4b

# Test with Gemma 4 E4B
MODEL=gemma4:e4b
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"${MODEL}\",\"prompt\":\"Please answer in Traditional Chinese. Use exactly 3 bullet points to explain what Docker, Ollama, and Gemma 4 do in this deployment.\",\"stream\":false}"

# Pull Gemma 4 26B when you want to switch
docker exec ollama ollama pull gemma4:26b

# Switch to Gemma 4 26B
MODEL=gemma4:26b
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"${MODEL}\",\"prompt\":\"Please answer in Traditional Chinese. Use exactly 3 bullet points to explain what Docker, Ollama, and Gemma 4 do in this deployment.\",\"stream\":false}"

# Show recent Ollama logs
docker logs --tail 100 ollama
