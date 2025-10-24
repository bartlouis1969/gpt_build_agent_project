# SECRETS_TEMPLATE.md

Vul deze secrets in als GitHub repository secrets of in je .env-bestand:

- `DISCORD_WEBHOOK_URL`: Webhook URL voor Discord alerts
- `GOOGLE_SHEETS_TOKEN`: Service account JSON voor Google Sheets API
- `GOOGLE_SHEETS_ID`: Naam of ID van je Google Sheet
- `NOTION_API_KEY`: Integratie-token voor Notion API
- `NOTION_DATABASE_ID`: Database ID voor Notion sync

Voorbeeld `.env`:
```env
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
GOOGLE_SHEETS_TOKEN={...json...}
GOOGLE_SHEETS_ID=FinanceTracker
NOTION_API_KEY=secret_xxx
NOTION_DATABASE_ID=xxx-xxx-xxx
```

Voeg deze secrets toe via GitHub > Settings > Secrets voor workflow-automatisering.
