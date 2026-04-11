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

> 先用 `openai/gpt-4o` 當範例。**不要直接把 Copilot CLI 看到的模型名稱原樣拿來給 Aider**；實際可用模型必須以 `https://api.githubcopilot.com/models` 回傳結果為準。

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

如果某個模型在 Aider 中報：

```text
model "<name>" is not accessible via the /chat/completions endpoint
```

代表它不是這個端點目前可用的 chat model，請改用 `/models` 回傳中真正存在的模型 ID。

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
/run <shell-command>
/test <shell-command>
/commit
/model <model-name>
/chat-mode code
/chat-mode ask
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

### 3-3. Aider 的工作模式要點

Aider **不是**像某些 agent CLI 那樣內建完整的 `read / write / bash` 工具系統。它的核心能力比較偏向：

| 類型 | Aider 行為 |
|---|---|
| 讀寫檔案 | 主要針對已加入聊天的檔案進行編輯 |
| Shell 指令 | 可用 `/run`、`/test` 執行命令，但不是完整代理式 bash 工具 |
| 多步自主操作 | 預設較弱，不會像全代理模式那樣自己規劃一整串動作 |
| 預設模式 | 通常是 `code` mode，但仍需要明確上下文與目標檔案 |

如果你直接說：

```text
請幫我寫一個 ToDo Web App
```

它很可能只會：

1. 直接在畫面上吐方案或程式碼
2. 要你先 `/add` 相關檔案
3. 或要求你先確認要建立哪些檔案

這不一定是壞掉，而是因為 Aider 比較偏向「在既有 repo 內編輯檔案」。

### 3-4. 想讓 Aider 真的動手改檔，建議這樣下

先把目標檔案加進去：

```text
/add package.json
/add src/App.tsx
/add src/main.tsx
```

如果檔案還不存在，可以直接明講要建立：

```text
/chat-mode code
請建立一個最小可運行的 ToDo Web App。
需求：
1. 建立需要的新檔案。
2. 不要只貼程式碼在聊天裡。
3. 直接修改 repo 內檔案。
4. 完成後告訴我有哪些檔案被建立或修改。
```

如果你想先討論方案，再讓它動手：

```text
/chat-mode ask
請先規劃這個 ToDo Web App 需要哪些檔案與技術。
```

確認後再切回：

```text
/chat-mode code
照剛剛的方案直接實作。
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

### 問題 2：模型名稱錯誤，Aider 提示 not accessible via /chat/completions

**症狀**
- 例如：`model "gpt-5.4-mini" is not accessible via the /chat/completions endpoint`

**常見原因**
- 直接把 Copilot CLI 或其他工具中的模型名稱拿來給 Aider
- 該模型不在 Copilot OpenAI-compatible `/models` 清單中

**解法**
1. 先查模型清單：

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

2. 從回傳結果挑一個實際存在的 ID
3. 用 `openai/<id>` 啟動 Aider，例如：

```bash
aider --model openai/gpt-4o
```

### 問題 3：本地 Ollama 連不上

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

### 問題 4：Aider 只把程式碼吐在畫面上，沒有真的改檔

**常見原因**
- 沒有先 `/add` 目標檔案
- 請求太大、太抽象，例如直接叫它「做一個完整 Web App」
- 目前不在 `code` mode
- 模型本身偏弱，比較傾向輸出說明而不是穩定產生 edits

**解法**
1. 先 `/add` 目標檔案，或明講要建立哪些新檔
2. 明確指定「直接修改檔案，不要只貼程式碼在聊天裡」
3. 先用 `/chat-mode ask` 討論，再切 `/chat-mode code`
4. 必要時換更強模型，例如：

```text
/model openai/gpt-4o
```

### 問題 5：`aider` 指令找不到

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
