# Step 003 — Docker GPU Runtime 驗證完成

## Input

| 項目 | 內容 |
|---|---|
| 已選方案 | A：Ollama (Docker) |
| 前置需求 | Docker 容器需可使用 NVIDIA GPU |

## Process

先提供 `nvidia-container-toolkit` 安裝與 Docker runtime 設定步驟，再要求使用者用 Docker image 驗證 GPU 是否可在容器中被看見。

## 已執行的驗證指令

```bash
docker run --rm --gpus all ubuntu:22.04 nvidia-smi
```

## 實際結果

```text
Sat Apr 11 03:18:55 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.126.09             Driver Version: 580.126.09     CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
|   0  NVIDIA GeForce RTX 2070 ...    Off |   00000000:01:00.0 Off |                  N/A |
| 24%   30C    P8             17W /  235W |      16MiB /   8192MiB |      0%      Default |
+-----------------------------------------------------------------------------------------+
```

## 判讀

| 項目 | 結論 |
|---|---|
| 問題性質 | 最初失敗原因是驗證 image tag 選錯，非 runtime 問題 |
| 是否代表 GPU 故障 | 否 |
| 是否代表 toolkit 失敗 | 否 |
| 最終驗證結論 | Docker 容器已可直接呼叫 `nvidia-smi`，GPU runtime 正常 |

## 後續動作

進入下一步：啟動 Ollama 容器。

## 目前狀態

本步已完成。
