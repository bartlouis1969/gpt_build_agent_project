#!/bin/bash
# railway.sh - Handige Railway CLI script voor lokaal testen en deploy

set -e

# 1. Installeer Railway CLI indien nodig
if ! command -v railway &> /dev/null; then
    echo "Railway CLI niet gevonden, installeren..."
    curl -fsSL https://railway.com/install.sh | sh
    export PATH="$HOME/.railway/bin:$PATH"
fi

# 2. Login (indien niet ingelogd)
echo "Railway login..."
railway login

# 3. Link project
PROJECT_ID="81625548-8db4-485e-87b1-48f85de7811d"
echo "Project koppelen... ($PROJECT_ID)"
railway link -p "$PROJECT_ID"

# 4. Secrets instellen (voorbeeld)
# railway variables:set OPENAI_API_KEY=sk-... MODEL_NAME=gpt-4
# railway variables:set DEFAULT_TEMPERATURE=0.7 MAX_TOKENS=1000 GPT_TIMEOUT=30

# 5. Lokaal deployen
railway up

# 6. Logs bekijken
# railway logs

# 7. Project openen in browser
# railway open

echo "✅ Railway CLI setup & lokale deploy voltooid!"
