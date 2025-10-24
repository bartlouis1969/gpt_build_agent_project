"""
budget_assistant.py

Geeft alerts bij overschrijding van budget en analyseert trends.
Voorbeeldgebruik:
    python budget_assistant.py --max 100
"""

import argparse
import os
from datetime import datetime

import pandas as pd  # type: ignore

FINANCE_DIR = os.path.dirname(__file__)
COSTS_FILE = os.path.join(FINANCE_DIR, "costs_tracker.csv")

parser = argparse.ArgumentParser(description="Budget Assistant")
parser.add_argument("--max", type=float, default=100.0, help="Maandelijks budget")
args = parser.parse_args()

costs = pd.read_csv(COSTS_FILE)
month = datetime.now().strftime("%Y-%m")
month_costs = costs[costs["date"].str.startswith(month)]
total = month_costs["amount"].sum()

if total > args.max:
    print(f"   Waarschuwing: maandelijkse uitgaven ({total:.2f}) ")
    print(f"overschrijden het budget ({args.max:.2f})!")
else:
    print(f"OK Uitgaven deze maand: {total:.2f} van maximaal {args.max:.2f}")

trend = month_costs.groupby("category")["amount"].sum().sort_values(ascending=False)
print("\nUitgaven per categorie:")
print(trend)
