# SETUP-GEMMA4-README

本文件整理本專案已驗證過的流程，說明如何在 **Ubuntu + Docker + Ollama** 環境下，建立一個**已預載 `gemma4:e4b` 與 `gemma4:26b`** 的自訂 image，之後直接用這個 image 啟動，不必每次重拉模型。

## 1. 目標環境

| 項目 | 規格 |
|---|---|
| OS | Ubuntu 24.04.3 LTS |
| CPU | Intel i7-10700 |
| RAM | 62 GiB |
| GPU | NVIDIA GeForce RTX 2070 SUPER 8GB |
| Driver | 580.126.09 |
| Docker | 29.2.0 |

## 2. 模型策略

| 模型 | 建議用途 | 硬體適配 |
|---|---|---|
| `gemma4:e4b` | 預設主力模型 | 適合 8GB VRAM，已實測可用 |
| `gemma4:26b` | 第二階段進階測試 | 可跑，但會大量依賴 CPU offload，速度較慢 |

## 3. 安裝 NVIDIA Container Toolkit

如果你的 Docker 尚未能使用 GPU，先執行：

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
  | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg

curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
  | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
  | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt update
sudo apt install -y nvidia-container-toolkit

sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

驗證 GPU 是否可在容器中使用：

```bash
docker run --rm --gpus all ubuntu:22.04 nvidia-smi
```

如果成功，應能在容器內看到 NVIDIA-SMI 與 GPU 資訊。

## 4. Build 預載 Gemma 4 模型的自訂 image

這一步會直接從 stdin 傳入 Dockerfile，不需要另外建立 Dockerfile 檔案。

```bash
docker build -t local/ollama-gemma4:latest -<<'EOF'
FROM ollama/ollama:latest

RUN ollama serve >/dev/null 2>&1 & pid=$! ; \
    while ! ollama list >/dev/null 2>&1; do sleep 1; done ; \
    ollama pull gemma4:e4b && \
    kill $pid && wait $pid || true

RUN ollama serve >/dev/null 2>&1 & pid=$! ; \
    while ! ollama list >/dev/null 2>&1; do sleep 1; done ; \
    ollama pull gemma4:26b && \
    kill $pid && wait $pid || true

RUN ollama serve >/dev/null 2>&1 & pid=$! ; \
    while ! ollama list >/dev/null 2>&1; do sleep 1; done ; \
    ollama pull gemma4:31b && \
    kill $pid && wait $pid || true
EOF
```

### 4-1. 驗證 image 已建立

```bash
docker images | grep local/ollama-gemma4
```

### 4-2. 重要說明

1. 這個 image 會很大，因為內含 `gemma4:e4b` 與 `gemma4:26b`。
2. **之後啟動容器時不要再掛 `-v ...:/root/.ollama`**，不然會把 image 裡已預載的模型覆蓋掉，看起來就像又要重新下載。
3. 未來如果你想更新模型版本，再重新執行一次這個 build 指令即可。

## 5. 用自訂 image 啟動 Ollama 容器

```bash
docker rm -f ollama 2>/dev/null || true

docker run -d \
  --name ollama \
  --restart unless-stopped \
  --gpus all \
  -p 11434:11434 \
  local/ollama-gemma4:latest
```

檢查容器與 API：

```bash
docker ps --filter name=ollama
curl http://localhost:11434/api/tags
docker exec ollama ollama list
```

若看到 `ollama` 為 `Up`，而 `ollama list` / `/api/tags` 已能看到 `gemma4:e4b` 與 `gemma4:26b`，代表自訂 image 啟動成功。

## 6. 啟動 Gemma 4 E4B

### 6-1. 互動 chat

```bash
docker exec -it ollama ollama run gemma4:e4b
```

### 6-2. 單次測試

```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:e4b",
    "prompt": "Reply with exactly one line: GEMMA4_E4B_OK",
    "stream": false
  }'
```

成功時應可看到：

```json
{"response":"GEMMA4_E4B_OK", ...}
```

### 6-3. 實際問答測試

```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:e4b",
    "prompt": "Please answer in Traditional Chinese. Explain in exactly 3 bullet points what Docker, Ollama, and Gemma 4 each do in this deployment.",
    "stream": false
  }'
```

查看最近日誌：

```bash
docker logs --tail 100 ollama
```

本專案已實測 `gemma4:e4b` 可正常回應，且在此機器上有 **42/43 layers offloaded to GPU**。

## 7. 啟動 Gemma 4 26B

### 7-1. 互動 chat

```bash
docker exec -it ollama ollama run gemma4:26b
```

### 7-2. 單次測試

```bash
docker exec -it ollama ollama run gemma4:26b "Please answer in Traditional Chinese. Use exactly 3 bullet points to explain what Docker, Ollama, and Gemma 4 do in this deployment."
```

## 8. 日常操作

### 8-1. 查看目前已安裝模型

```bash
docker exec ollama ollama list
```

### 8-2. 查看 API 可見模型

```bash
curl http://localhost:11434/api/tags
```

### 8-3. 查看最近日誌

```bash
docker logs --tail 100 ollama
```

### 8-4. 停止 / 啟動容器

```bash
docker stop ollama
docker start ollama
```

## 9. 建議使用方式

| 情境 | 建議模型 |
|---|---|
| 日常本地開發、互動 chat | `gemma4:e4b` |
| 想測更大模型品質 | `gemma4:26b` |
| 8GB VRAM 主機的穩定預設值 | `gemma4:e4b` |

## 10. 注意事項

1. **`gemma4:e4b` 是目前這台機器的主力選擇。**
2. **`gemma4:26b` 可以跑，但會明顯變慢。**
3. 如果 `docker exec` 報錯容器不存在，先確認是否已完成第 5 步的 `docker run -d ...`。
4. 如果 API 沒回應，先檢查：

```bash
docker ps --filter name=ollama
docker logs --tail 100 ollama
```

5. 如果你用了 `-v some-volume:/root/.ollama`，image 內建模型會被蓋掉，之後又會變成需要重新拉模型。

## 11. 最短路徑

如果你只是要快速重建可用環境，照這個順序跑：

```bash
docker build -t local/ollama-gemma4:latest -<<'EOF'
FROM ollama/ollama:latest

RUN /bin/sh -c '\
    ollama serve >/tmp/ollama-build.log 2>&1 & \
    pid=$!; \
    i=0; \
    until ollama list >/dev/null 2>&1; do \
      i=$((i+1)); \
      if [ "$i" -ge 60 ]; then \
        cat /tmp/ollama-build.log; \
        exit 1; \
      fi; \
      sleep 1; \
    done; \
    ollama pull gemma4:e4b && \
    ollama pull gemma4:26b && \
    kill $pid && \
    wait $pid || true'
EOF

docker rm -f ollama 2>/dev/null || true

docker run -d \
  --name ollama \
  --restart unless-stopped \
  --gpus all \
  -p 11434:11434 \
  local/ollama-gemma4:latest

docker exec -it ollama ollama run gemma4:e4b
```
