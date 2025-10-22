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
