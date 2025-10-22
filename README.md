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
