"""
notion_sync.py

Synchroniseert kosten en credits met Notion via notion-client.
Voorbeeldgebruik:
    python notion_sync.py --token <integration_token> --db <database_id>
"""

import argparse
import os

import pandas as pd  # type: ignore
from notion_client import Client  # type: ignore

FINANCE_DIR = os.path.dirname(__file__)
COSTS_FILE = os.path.join(FINANCE_DIR, "costs_tracker.csv")
CREDITS_LOG = os.path.join(FINANCE_DIR, "credits_log.csv")

parser = argparse.ArgumentParser(description="Notion Sync")
parser.add_argument("--token", type=str, required=True, help="Notion integration token")
parser.add_argument("--db", type=str, required=True, help="Notion database ID")
args = parser.parse_args()

notion = Client(auth=args.token)
costs = pd.read_csv(COSTS_FILE)
credits = pd.read_csv(CREDITS_LOG) if os.path.exists(CREDITS_LOG) else pd.DataFrame()

# Kosten naar Notion
for _, row in costs.iterrows():
    notion.pages.create(
        parent={"database_id": args.db},
        properties={
            "Date": {"date": {"start": row["date"]}},
            "Category": {"title": [{"text": {"content": row["category"]}}]},
            "Amount": {"number": float(row["amount"])},
            "Description": {"rich_text": [{"text": {"content": row["description"]}}]},
            "User": {"rich_text": [{"text": {"content": row["user"]}}]},
        },
    )

# Credits naar Notion
for _, row in credits.iterrows():
    notion.pages.create(
        parent={"database_id": args.db},
        properties={
            "Timestamp": {"date": {"start": row["timestamp"]}},
            "User": {"rich_text": [{"text": {"content": row["user"]}}]},
            "Action": {"rich_text": [{"text": {"content": row["action"]}}]},
            "Amount": {"number": float(row["amount"])},
            "Balance": {"number": float(row["balance"])},
        },
    )

print("Notion sync voltooid.")
