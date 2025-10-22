# GPT Build Agent Project

This project is a self-improving, test-driven AI agent framework with FastAPI endpoints, full test coverage, CI/CD via GitHub Actions, and ready for deployment on Railway using Docker.

## Features

- Volatility analytics module
- AI content generator module
- FastAPI endpoints for analytics and AI
- Full unit and endpoint tests
- CI/CD pipeline
- Ready for Docker/Railway deployment

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

## AI Memory Endpoint

Nieuwe endpoint: `/ai/memory`

- **POST /ai/memory**: Sla een geheugenwaarde op met een key en value.
- **GET /ai/memory/{key}**: Haal een specifieke geheugenwaarde op.
- **GET /ai/memory**: Haal alle geheugenentries op.

Voorbeeld:

```json
POST /ai/memory
{
  "key": "user_note",
  "value": "Dit is een testgeheugen."
}
```

Zie ook: `app/routes/memory.py` en unittests in `app/routes/test_memory.py`.

## Analytics: Signaaldetectie & Backtest

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

Statistieken worden nu berekend op basis van de input:

- **score**: gemiddeld rendement per trade
- **risk**: standaarddeviatie van rendementen
- **volatility**: standaarddeviatie van prijsveranderingen
- **sharpe_ratio**: verhouding rendement/risico
- **max_drawdown**: grootste daling vanaf piek

Zie ook: `app/routes/signal_check.py` en unittests in `tests/test_signal_check.py`.
