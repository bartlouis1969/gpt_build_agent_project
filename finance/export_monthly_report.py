"""
export_monthly_report.py

Exporteert kosten en creditsbalans per maand naar exports/YYYY-MM.csv.
Automatisch te draaien via CRON, CI of handmatig.

Voorbeeldgebruik:
    python export_monthly_report.py
"""

import os
from datetime import datetime

import pandas as pd  # type: ignore

FINANCE_DIR = os.path.dirname(__file__)
COSTS_FILE = os.path.join(FINANCE_DIR, "costs_tracker.csv")
CREDITS_LOG = os.path.join(FINANCE_DIR, "credits_log.csv")
EXPORTS_DIR = os.path.join(FINANCE_DIR, "..", "exports")

os.makedirs(EXPORTS_DIR, exist_ok=True)

month = datetime.now().strftime("%Y-%m")
export_file = os.path.join(EXPORTS_DIR, f"{month}.csv")

costs = pd.read_csv(COSTS_FILE)
try:
    credits = pd.read_csv(CREDITS_LOG)
except FileNotFoundError:
    credits = pd.DataFrame(columns=["timestamp", "user", "action", "amount", "balance"])

with open(export_file, "w", encoding="utf-8") as f:
    f.write("# Kostenoverzicht\n")
    costs.to_csv(f, index=False)
    f.write("\n# Creditslog\n")
    credits.to_csv(f, index=False)

print(f"Export voltooid: {export_file}")
