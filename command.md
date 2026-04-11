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
