# Automatisering & Alerts

Je project bevat nu drie krachtige workflows voor financiële controle:

## 1. Maandelijkse export

- Workflow: `.github/workflows/monthly_export.yml`
- Trigger: 1e van de maand
- Resultaat: CSV-export in `reports/`

## 2. Budgetoverschrijding alerts

- Workflow: `.github/workflows/budget_alerts.yml`
- Trigger: dagelijks & bij push
- Resultaat: Discord-alert bij overschrijding
- Placeholder: `DISCORD_WEBHOOK_URL`

## 3. Dagelijkse sync

- Workflow: `.github/workflows/sync_finance.yml`
- Trigger: dagelijks
- Resultaat: Sync naar Google Sheets & Notion
- Placeholders: `GOOGLE_SHEETS_TOKEN`, `GOOGLE_SHEETS_ID`, `NOTION_API_KEY`, `NOTION_DATABASE_ID`

## Secrets instellen

Zie `SECRETS_TEMPLATE.md` voor alle benodigde variabelen. Voeg deze toe via GitHub > Settings > Secrets of in `.env`.

## Activatie

- Vul de secrets in
- Push naar GitHub
- Workflows draaien automatisch

Je ontvangt alerts, exports en synchronisaties zonder handmatige acties. Vervang placeholders voor je eigen integraties.
