"""
google_sheets_sync.py

Synchroniseert kosten en credits met Google Sheets via gspread.
Voorbeeldgebruik:
    python google_sheets_sync.py --sheet "FinanceTracker"
"""

import argparse
import os

import gspread  # type: ignore
import pandas as pd  # type: ignore
from oauth2client.service_account import ServiceAccountCredentials  # type: ignore

FINANCE_DIR = os.path.dirname(__file__)
COSTS_FILE = os.path.join(FINANCE_DIR, "costs_tracker.csv")
CREDITS_LOG = os.path.join(FINANCE_DIR, "credits_log.csv")

parser = argparse.ArgumentParser(description="Google Sheets Sync")
parser.add_argument("--sheet", type=str, required=True, help="Google Sheet name")
args = parser.parse_args()

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
gc = gspread.authorize(creds)

sheet = gc.open(args.sheet)
costs = pd.read_csv(COSTS_FILE)
credits = pd.read_csv(CREDITS_LOG) if os.path.exists(CREDITS_LOG) else pd.DataFrame()

# Kosten naar sheet
ws_titles = [ws.title for ws in sheet.worksheets()]
if "Costs" in ws_titles:
    costs_ws = sheet.worksheet("Costs")
else:
    costs_ws = sheet.add_worksheet(title="Costs", rows="100", cols="10")
costs_ws.clear()
costs_ws.update([costs.columns.values.tolist(), *costs.values.tolist()])

# Credits naar sheet
if "Credits" in ws_titles:
    credits_ws = sheet.worksheet("Credits")
else:
    credits_ws = sheet.add_worksheet(title="Credits", rows="100", cols="10")
credits_ws.clear()
credits_ws.update([credits.columns.values.tolist(), *credits.values.tolist()])

print("Google Sheets sync voltooid.")
