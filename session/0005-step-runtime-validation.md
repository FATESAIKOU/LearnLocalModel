# Step 003 — Docker GPU Runtime 驗證現況

## Input

| 項目 | 內容 |
|---|---|
| 已選方案 | A：Ollama (Docker) |
| 前置需求 | Docker 容器需可使用 NVIDIA GPU |

## Process

先提供 `nvidia-container-toolkit` 安裝與 Docker runtime 設定步驟，再要求使用者用 Docker image 驗證 GPU 是否可在容器中被看見。

## 已執行的驗證指令

```bash
docker run --rm --gpus all nvidia/cuda:12.0-base-ubuntu22.04 nvidia-smi
```

## 實際結果

```text
Unable to find image 'nvidia/cuda:12.0-base-ubuntu22.04' locally
docker: Error response from daemon: manifest for nvidia/cuda:12.0-base-ubuntu22.04 not found: manifest unknown: manifest unknown
```

## 判讀

| 項目 | 結論 |
|---|---|
| 問題性質 | 驗證 image tag 不存在 |
| 是否代表 GPU 故障 | 否 |
| 是否代表 toolkit 必定失敗 | 否 |

## 後續動作

已要求使用者回報：

```bash
nvidia-ctk --version
```

## 目前狀態

使用者口頭回覆「有了」，但尚未提供實際版本輸出，因此本步仍視為**驗證中**。
