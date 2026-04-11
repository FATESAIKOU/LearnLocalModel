# Aider Setup Guide

本文件整理本專案已完成的 Aider 配置流程，目標是建立一套 **雙引擎熱切換** 的結對編程環境：

- **本地端**：Ollama
- **雲端端**：GitHub Copilot OpenAI-compatible API
- **工具層**：Aider

## 1. 從零開始的配置步驟

### 1-1. 安裝系統基礎套件

```bash
sudo apt update
sudo apt install -y python3 python3-pip git

python3 --version
python3 -m pip --version
git --version
```

### 1-2. 安裝 Aider

```bash
python3 -m pip install --user -U aider-chat

aider --version || ~/.local/bin/aider --version
```

如果 `aider` 不在 PATH，可以改用：

```bash
~/.local/bin/aider --version
```

### 1-3. 進入專案並確認 Git 狀態

```bash
cd /home/fatesaikou/testAI/LearnLocalModel

pwd
git rev-parse --show-toplevel
git rev-parse --is-inside-work-tree
git --no-pager status --short
```

### 1-4. 建立 `.env`

以下指令會從 `~/.config/github-copilot/apps.json` 讀取 `oauth_token`，並寫入專案 `.env`：

```bash
COPILOT_TOKEN="$(python3 - <<'PY'
import json
from pathlib import Path

path = Path.home() / ".config/github-copilot/apps.json"
data = json.loads(path.read_text())

def find_token(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get("oauth_token"), str) and obj["oauth_token"]:
            return obj["oauth_token"]
        for value in obj.values():
            token = find_token(value)
            if token:
                return token
    elif isinstance(obj, list):
        for value in obj:
            token = find_token(value)
            if token:
                return token
    return ""

print(find_token(data), end="")
PY
)"

test -n "$COPILOT_TOKEN"

cat > .env <<EOF
OLLAMA_API_BASE=http://127.0.0.1:11434
OPENAI_API_BASE=https://api.githubcopilot.com
OPENAI_API_KEY=${COPILOT_TOKEN}
EOF
```

### 1-5. 驗證 `.env`

```bash
grep -E '^(OLLAMA_API_BASE|OPENAI_API_BASE)=' .env

python3 - <<'PY'
from pathlib import Path

env = {}
for line in Path(".env").read_text().splitlines():
    if "=" in line:
        key, value = line.split("=", 1)
        env[key] = value

print("OPENAI_API_KEY_present=", bool(env.get("OPENAI_API_KEY")))
print("OPENAI_API_KEY_length=", len(env.get("OPENAI_API_KEY", "")))
PY
```

### 1-6. 載入 `.env`

每次開新 shell 要跑：

```bash
cd /home/fatesaikou/testAI/LearnLocalModel
set -a
source .env
set +a
```

## 2. 日常使用指南

### 2-1. 啟動 Aider（本地模型）

官方建議 Ollama 模型優先用 `ollama_chat/` 前綴。

```bash
cd /home/fatesaikou/testAI/LearnLocalModel
set -a
source .env
set +a

aider --model ollama_chat/gemma4:e4b
```

### 2-2. 啟動 Aider（雲端 Copilot 模型）

```bash
cd /home/fatesaikou/testAI/LearnLocalModel
set -a
source .env
set +a

aider --model openai/gpt-4o
```

> `openai/gpt-4o` 只是範例。實際可用模型取決於你的 Copilot 訂閱。

### 2-3. 查詢 Copilot 可用模型

```bash
cd /home/fatesaikou/testAI/LearnLocalModel
set -a
source .env
set +a

curl -s https://api.githubcopilot.com/models \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Copilot-Integration-Id: vscode-chat"
```

把回傳中的模型 ID 前面加上 `openai/`，就能給 Aider 使用，例如：

```bash
aider --model openai/gpt-4o
aider --model openai/claude-3.7-sonnet-thought
```

### 2-4. 把檔案加入上下文

進入 Aider 後，使用：

```text
/add path/to/file
```

例如：

```text
/add command.md
/add SETUP-GEMMA4-README.md
```

### 2-5. 在本地與雲端模型間無縫熱切換

在同一個 Aider session 內，用：

```text
/model ollama_chat/gemma4:e4b
```

切回本地模型，或：

```text
/model openai/gpt-4o
```

切到雲端 Copilot 模型。

如果你的 Copilot 帳號可用其他模型，也可以替換成實際模型 ID：

```text
/model openai/claude-3.7-sonnet-thought
```

### 2-6. 常用 Aider 指令

```text
/add path/to/file
/drop path/to/file
/ls
/diff
/commit
/model <model-name>
/help
/exit
```

## 3. 建議工作流

### 3-1. 快速開始

```bash
cd /home/fatesaikou/testAI/LearnLocalModel
set -a
source .env
set +a

aider --model ollama_chat/gemma4:e4b
```

進入後：

```text
/add path/to/file
請幫我修改這個功能，並保持原本行為不變。
```

### 3-2. 需要更強模型時

直接在同一個 session 切換：

```text
/model openai/gpt-4o
```

任務完成後再切回本地：

```text
/model ollama_chat/gemma4:e4b
```

## 4. 常見問題與排錯

### 問題 1：Copilot API 出現 forbidden / 無法呼叫

**症狀**
- Aider 切到 `openai/...` 模型後報 403 或 forbidden

**常見原因**
- `~/.config/github-copilot/apps.json` 裡的 token 已過期
- token 不是具備正確 scope 的 Copilot OAuth token

**解法**
1. 重新在 JetBrains IDE 重新登入 GitHub Copilot
2. 重新執行 `.env` 建立步驟，把新 token 寫回 `.env`
3. 重新 `source .env`

### 問題 2：本地 Ollama 連不上

**症狀**
- `aider --model ollama_chat/gemma4:e4b` 無法連線
- 或 Aider 提示 Ollama API 不可用

**常見原因**
- Ollama container 沒有啟動
- `OLLAMA_API_BASE` 沒有正確 export

**解法**
1. 檢查 Ollama：

```bash
docker ps --filter name=ollama
curl http://127.0.0.1:11434/api/tags
```

2. 確認 shell 內已載入 `.env`：

```bash
set -a
source .env
set +a
echo "$OLLAMA_API_BASE"
```

### 問題 3：`aider` 指令找不到

**解法**

```bash
~/.local/bin/aider --version
```

如果這條可用，就代表只是 PATH 尚未包含 `~/.local/bin`。

## 5. 總結

這個專案目前已具備：

1. **本地 Aider + Ollama (`gemma4:e4b`)**
2. **雲端 Aider + GitHub Copilot (`openai/...`)**
3. **在同一個 Aider session 內用 `/model` 做雙引擎熱切換**
4. **用 `/add` 精準控制上下文檔案**
