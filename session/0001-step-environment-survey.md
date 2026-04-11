# Step 001 — 環境調查

## Input

| 項目 | 內容 |
|---|---|
| 伺服器 | Ubuntu Server |
| 已知硬體 | i7-10700 / 64GB RAM / RTX 2070 SUPER 8GB VRAM |

## Process

要求使用者執行環境檢查指令，收集 OS、Kernel、CPU、RAM、GPU、Driver、CUDA、Docker、Python、Disk 狀態。

## Output

| 項目 | 結果 |
|---|---|
| OS | Ubuntu 24.04.3 LTS |
| Kernel | 6.8.0-107-generic |
| CPU | Intel i7-10700 / 16 threads |
| RAM | 62Gi |
| GPU | RTX 2070 SUPER |
| Driver | 580.126.09 |
| CUDA Toolkit | 未安裝 |
| Docker | 29.2.0 |
| Python | 3.12.7 |
| Disk | 1.5TB free |

## 結論

這台機器可以執行 Gemma 4，但要以 **8GB VRAM** 為核心限制來設計部署方案。
