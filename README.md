# GPT Build Agent Project

[![codecov](https://codecov.io/gh/bartlouis1969/gpt_build_agent_project/branch/main/graph/badge.svg)](https://codecov.io/gh/bartlouis1969/gpt_build_agent_project)

## 🚀 Draaiboek & Quick Start

Welkom bij het GPT Build Agent Project! Dit project bevat een compleet draaiboek met alle stappen, instellingen en uitbreidingen voor de AI-agent, EA-integratie, domeinkoppeling, CI/CD, brokers, deployment en meer.

- **Draaiboek:** Zie het bestand `EA_test_checklist.md` voor het volledige overzicht van alle stappen en best practices.
- **Quick Start:**
    1. Clone deze repository.
    2. Voer het setup script uit: `python setup_agent.py` (zie onder).
    3. Volg de instructies in het draaiboek en het script voor een vliegende start.
    4. Bekijk de secties hieronder voor meer details over features, deployment en plugins.

> 📖 **Tip:** Het draaiboek is altijd actueel en overdraagbaar. Ideaal voor nieuwe teamleden, testers en als geheugensteun voor jezelf.

---

## 🧪 Test & Pre-commit Workflow

### Foutloos testen

1. Open terminal 1, activeer je omgeving, en start de server:

    ```pwsh
    python -m app.main
    ```

    Laat deze terminal open zodat de server actief blijft.
2. Open terminal 2, activeer opnieuw je omgeving, en voer de tests uit:

    ```pwsh
    pytest --maxfail=1 --disable-warnings
    ```

### Pre-commit setup

1. Installeer pre-commit:

    ```pwsh
    pip install pre-commit
    ```

2. Voeg het configuratiebestand `.pre-commit-config.yaml` toe (zie hieronder).
3. Activeer pre-commit hooks:

    ```pwsh
    pre-commit install
    ```

Nu wordt je code automatisch gecontroleerd (lint, formatting, etc.) vóór elke commit.
Voorbeeld `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: "https://github.com/psf/black"
    rev: 24.3.0
    hooks:
      - id: black
  - repo: "https://github.com/PyCQA/flake8"
    rev: 7.0.0
    hooks:
      - id: flake8
  - repo: "https://github.com/pre-commit/mirrors-autopep8"
    rev: v2.0.4
    hooks:
      - id: autopep8
```

---

## 📄 Overdrachtsdocument & Stappenplan

Het volledige overdrachtsdocument en stappenplan vind je hier:

- [Transfer Plan (Markdown)](docs/transfer_plan.md)
- [Transfer Plan (PDF, automatisch gegenereerd)](exports/transfer_plan.pdf)

Gebruik dit als onboardinggids voor nieuwe teamleden, adviseurs en co-agents. Je kunt het document ook delen via e-mail of als bijlage bij een GitHub-release.

---

Welkom bij het GPT Build Agent Project! Dit project bevat een compleet draaiboek met alle stappen, instellingen en uitbreidingen voor de AI-agent, EA-integratie, domeinkoppeling, CI/CD, brokers, deployment en meer.

- **Draaiboek:** Zie het bestand `EA_test_checklist.md` voor het volledige overzicht van alle stappen en best practices.
- **Quick Start:**
    1. Clone deze repository.
    2. Voer het setup script uit: `python setup_agent.py` (zie onder).
    3. Volg de instructies in het draaiboek en het script voor een vliegende start.
    4. Bekijk de secties hieronder voor meer details over features, deployment en plugins.

> 📖 **Tip:** Het draaiboek is altijd actueel en overdraagbaar. Ideaal voor nieuwe teamleden, testers en als geheugensteun voor jezelf.

---

This project is a self-improving, test-driven AI agent framework with FastAPI endpoints, full test coverage, CI/CD via GitHub Actions, and ready for deployment on Railway using Docker.



## Features

- Volatility analytics module
- AI content generator module
- FastAPI endpoints for analytics and AI
- Full unit and endpoint tests
- CI/CD pipeline
- Ready for Docker/Railway deployment
- 📘 Game: speelmechaniek en design ([game_script.md](docs/game_script.md))
- 🧠 Evolutionair tradingplatform: zelflerende EA, FTMO-bescherming, copy trading, premium signalen, accountbeheer. Zie [game_design.md](docs/game_design.md) en modules: `ea_config.py`, `mt5_connector.py`, `player_settings.py`.

## Quickstart

1. Clone the repo
2. Add your environment variables (e.g. `OPENAI_API_KEY`)
3. Build and run with Docker:

   ```sh
   docker build -t gpt-agent .
   docker run -p 8000:8000 gpt-agent
   ```

4. Visit `http://localhost:8000/health` to check status

## Railway Deployment

- Push to GitHub
- Connect repo to Railway
- Deploy using Dockerfile

## Environment Variables

- `OPENAI_API_KEY` (required)
- `MODEL_NAME`, `DEFAULT_TEMPERATURE`, `MAX_TOKENS`, `GPT_TIMEOUT` (optional)

## License

MIT


## Project Architecture Overview

```mermaid
graph TD
    subgraph FastAPI Backend
        A[main.py] --> B[Routes]
        B --> C[/ai/generate endpoint]
        B --> D[/volatility endpoint]
    end

    subgraph AI Functionaliteit
        C --> E[core/ai/generator.py]
        E --> F[OpenAI API]
    end

    subgraph Analytics
        D --> G[core/analytics/volatility.py]
    end

    subgraph Config & Environment
        H[config/loader.py] --> A
        H --> E
        H --> G
    end

    subgraph Testing
        I[Unittests & Endpointtests]
        I --> E
        I --> G
        I --> B
    end

    subgraph CI/CD
        J[GitHub Actions]
        J --> I
        J --> K[Lint (flake8, black, ruff)]
        J --> L[Deploy (Docker, Railway)]
    end

    subgraph Deployment
        L --> M[Railway Cloud]
        L --> N[railway.sh (lokaal)]
    end

    subgraph Self-Improvement
        O[Testfailures]
        O --> P[lessons.json]
        P --> J
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px
    style G fill:#bfb,stroke:#333,stroke-width:2px
    style H fill:#ffd,stroke:#333,stroke-width:2px
    style I fill:#eee,stroke:#333,stroke-width:2px
    style J fill:#ccf,stroke:#333,stroke-width:2px
    style L fill:#fcf,stroke:#333,stroke-width:2px
    style O fill:#fee,stroke:#333,stroke-width:2px
```

Dit diagram toont de hoofdcomponenten, hun relaties en de AI-stromen (van endpoint tot deployment en self-improvement). Je kunt deze Mermaid-code direct in je README of een Markdown-viewer gebruiken voor een visueel overzicht!



## Plugin-systeem voor uitbreidbare AI-agent

Nieuwe feature: plugins kunnen eenvoudig worden toegevoegd in de map `plugins/`.

- Elk Python-bestand in `plugins/` met een FastAPI `router` wordt automatisch geladen.
- Plugins kunnen eigen endpoints en logica bevatten.

Voorbeeldplugin:

```python
# plugins/hello_plugin.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/plugin/hello")
def hello_plugin():
    return {"message": "Hello from plugin!"}
```

Na toevoegen is de endpoint `/plugin/hello` direct beschikbaar.

Zie ook: plugin loader in `app/main.py`.

Nieuwe endpoint: `/ai/feedback`

- **POST /ai/feedback**: Sla feedback op voor retraining/self-improvement.
- **GET /ai/feedback**: Haal alle feedback entries op.

Feedback wordt opgeslagen in `lessons.json` en gebruikt voor het verbeteren van de agent.

Voorbeeld:

```json
POST /ai/feedback
{
    "user": "admin",
    "feedback": "De AI-strategie werkt goed, maar kan sneller reageren op volatiliteit."
}
```

Zie ook: `app/routes/feedback.py` en het lessons.json-bestand.


## Trading Performance Tracker

Nieuwe endpoint: `/analytics/performance`

- **POST /analytics/performance**: Voeg een trade/resultaat toe met KPIs.
- **GET /analytics/performance**: Haal alle cumulatieve KPIs en trades op.

Data wordt opgeslagen in `performance.json` en bevat:
    - totaal aantal trades
    - totaal en gemiddeld rendement (pnl)
    - gemiddeld risico
    - maximale drawdown
    - alle trades met timestamp, pnl, risk, drawdown, notes

Voorbeeld toevoegen:

```json
POST /analytics/performance
{
    "timestamp": "2025-10-23T12:00:00Z",
    "pnl": 120.5,
    "risk": 0.35,
    "drawdown": -0.08,
    "notes": "Test trade entry."
}
```

Voorbeeld ophalen:

```json
GET /analytics/performance
{
    "total_trades": 1,
    "total_pnl": 120.5,
    "avg_pnl": 120.5,
    "avg_risk": 0.35,
    "max_drawdown": -0.08,
    "trades": [ ... ]
}
```

Zie ook: `app/routes/performance.py` en het performance.json-bestand.

Nieuwe endpoint: `/analytics/signal-check`

- **POST /analytics/signal-check**: Evalueer trading-signalen op score, risico, volatiliteit en tradingstatistieken.

**Input:**

```json
{
  "signal": [1, 0, 1, -1, 0],         // 1=buy, 0=hold, -1=sell
  "prices": [100, 102, 101, 105, 103],
  "risk_level": "medium",            // optioneel: low | medium | high
  "portfolio_value": 10000             // optioneel: voor sizing/simulatie
}
```

**Output:**

```json
{
  "score": 0.82,
  "risk": 0.45,
  "volatility": 0.12,
  "details": {
    "trades_executed": 3,
    "sharpe_ratio": 1.12,
    "max_drawdown": 0.06
  }
}
```


---

## 🔭 Fase na GPT-Agent + EA = “AI Core Expansion”

Je project evolueert naar een AI-gedreven ecosysteem. Hieronder de logische groeistappen, opgedeeld in 3 strategische gebieden:

### 💡 1. AI-Driven Niche Modules (Post-launch uitbreidingen)

| Richting                  | Beschrijving                                                                  | Voorbeeldmodules                                                    |
| ------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 🧠 Self-Improving Finance | Laat de EA zelfmarkten leren & strategisch aanpassen                          | Auto-optimizing EA, live market classifier                          |
| 📚 EdTech                 | Combineer GPT met educatieve scenario’s                                       | “AI leert je traden” module                                         |
| 🎮 GPT x Gaming           | Maak een spel waarin GPT real-time meespeelt of de wereld bestuurt            | GPT-dungeon-achtig spel dat samenwerkt met jouw EA/agent            |
| 🗃️ Plugin-platform       | Breid je systeem modulair uit met plugins (bijv. news-scraper, signal-voters) | Plugin voor Telegram alerts, TradingView analyse, nieuwsfeed-parser |

### 🎮 2. Spel-geïntegreerde AI & Trading

## Spelidee: "TradeQuest – AI vs. Market"

- 🎯 Doel: Speler moet met hulp van een AI-agent trading-uitdagingen voltooien in een gamified omgeving.
- 🤖 AI-rol: NPC’s of medespelers met GPT-intelligentie, of GPT als je coach.
- 📈 Live Market Feed: Gebruik de EA als backend-logica om trades te simuleren of live te spelen.
- 🔄 Realtime Integratie: AI-agent adviseert in-game, EA voert uit in demo/live.
- 🛠️ Tech Stack: Unity of Godot + Python FastAPI bridge + GPT4/GPTs.

> ✅ Uniek selling point: Je AI is niet alleen helper, maar speelt *mee* in het spel.

### 🌐 3. Van project naar platform

| Stap                            | Toelichting                                                               |
| ------------------------------- | ------------------------------------------------------------------------- |
| 🧩 Modules scheiden             | Maak je codebase modulair: `agent/`, `ea/`, `game/`, `api/`               |
| 🧠 Persistent AI-memory         | Laat je agent leren over gebruikers, markten, patronen                    |
| 🔌 Externe API’s integreren     | TradingView webhooks, nieuwsfeeds, Signal groups                          |
| 🧑‍🤝‍🧑 Meerdere agenten         | Laat meerdere AI-agenten taken uitvoeren of samenwerken                   |
| 🌍 Marketplace of Network       | Laat gebruikers eigen agents maken, trainen of inzetten (GPT + backtests) |

---

## 🚀 Roadmap & Fases

| Fase                 | Status        | Actie                                 |
| -------------------- | ------------- | ------------------------------------- |
| 1. Foundation        | ✅ Klaar       | Architectuur, CI/CD, AI-core          |
| 2. Trading/EA        | 🔄 Bijna af   | Laatste optimalisaties                |
| 3. AI-agent          | 🔄 Bijna af   | Self-improvement & commando-interface |
| 4. Expansion modules | 🧠 Startklaar | Game, plugins, GPT tools              |
| 5. Platformisatie    | 🔜            | Agent manager, dashboards, user roles |

---


---

## ⚡ Automatisering & Alerts

Je project bevat nu volledige automatisering voor financiële monitoring en synchronisatie:

### Workflows

| Workflow                | Trigger                | Functie                                              |
|-------------------------|------------------------|------------------------------------------------------|
| monthly_export.yml      | 1e van de maand        | Maakt maandelijkse export van kosten/credits         |
| budget_alerts.yml       | Dagelijks & bij push   | Stuurt Discord-alert bij budgetoverschrijding        |
| sync_finance.yml        | Dagelijks              | Synchroniseert data met Google Sheets & Notion       |

### Secrets & Placeholders

Vul deze in via GitHub > Settings > Secrets of in `.env`:

- `DISCORD_WEBHOOK_URL`: Webhook URL voor Discord alerts
- `GOOGLE_SHEETS_TOKEN`: Service account JSON voor Google Sheets API
- `GOOGLE_SHEETS_ID`: Naam of ID van je Google Sheet
- `NOTION_API_KEY`: Integratie-token voor Notion API
- `NOTION_DATABASE_ID`: Database ID voor Notion sync

Zie ook: `SECRETS_TEMPLATE.md` voor een overzicht.

### Activatie

1. Vul de secrets in
2. Push naar GitHub
3. Workflows draaien automatisch volgens schema

Je ontvangt alerts, exports en synchronisaties zonder handmatige acties. Vervang placeholders voor je eigen integraties.

---

## Environment variables

| Var                 | Default              | Uitleg |
|---------------------|----------------------|--------|
| `APP_BASE_URL`      | `http://127.0.0.1:8000` | Base-URL voor integratietests (token/performance checks). |
| `OPENAI_API_KEY`    | _(leeg)_             | Echte key triggert echte OpenAI-calls. Leeg, `sk-test*`, `dummy` of `placeholder` gebruikt de stub. |
| `OPENAI_MODEL`      | `gpt-4`              | Modelnaam voor echte OpenAI-calls. |
| `TRAINER_DAEMON_DEBUG` | `0`               | Zet op `1` om de trainer-daemon kort te laten “slapen” bij lokaal testen. |

### Test-stubbing

- In `core/ai/generator.py` zit een veilige fallback: zonder geldige `OPENAI_API_KEY` wordt **geen** netwerkcall gedaan en komt er een deterministisch resultaat terug.
- In `conftest.py` draait tijdens tests een mini stub-server voor `POST /ai/generate` (lokaal). Hierdoor zijn tests offline en snel.
- Testprofielen:
  - Unit suite (zonder integratie):
    ```bash
    pytest -q -m "not integration"
    ```
  - Volledige suite (start je FastAPI-app lokaal):
    ```bash
    uvicorn app.main:app --reload
    pytest -q
    ```

### Code style

- `isort`, `black`, `flake8` staan geconfigureerd.
  Snelle check:
  ```bash
  isort .; black .; flake8
  ```
