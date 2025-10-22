# Changelog

## v0.1.0 - Eerste publieke release

- 🚀 Initial deploy commit with Docker + FastAPI app
- Lint tooling re-install & fixes
- Volledige testdekking en CI/CD integratie
- Railway deployment scripts toegevoegd
- Architectuurdiagram en README verbeterd

## [v0.2.0] - 2024-06-07

### Toegevoegd

- Nieuwe endpoint `/ai/memory` voor het opslaan en ophalen van geheugenwaarden via POST/GET.
- Unittests toegevoegd voor geheugenendpoint (`app/routes/test_memory.py`).

## [v0.3.0] - 2025-10-22

### Nieuw

- Nieuwe endpoint `/analytics/signal-check` voor realtime evaluatie van trading-signalen (score, risico, volatiliteit, trades_executed, sharpe_ratio, max_drawdown).
- Unittests toegevoegd voor signal-check (`tests/test_signal_check.py`).
