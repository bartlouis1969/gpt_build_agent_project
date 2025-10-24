"""
dashboard.py

Streamlit-dashboard voor visuele monitoring van uitgaven en credits.
Start met: streamlit run dashboard.py
"""

import os

import pandas as pd  # type: ignore
import streamlit as st  # type: ignore

FINANCE_DIR = os.path.dirname(__file__)
COSTS_FILE = os.path.join(FINANCE_DIR, "costs_tracker.csv")
CREDITS_LOG = os.path.join(FINANCE_DIR, "credits_log.csv")

st.title("Finance Dashboard")

costs = pd.read_csv(COSTS_FILE)
credits = pd.read_csv(CREDITS_LOG) if os.path.exists(CREDITS_LOG) else None

st.header("Maandelijkse uitgaven")
month = pd.to_datetime(costs["date"]).dt.to_period("M")
monthly = costs.groupby(month)["amount"].sum()
st.bar_chart(monthly)

st.header("Uitgaven per categorie")
cat = costs.groupby("category")["amount"].sum()
st.bar_chart(cat)

if credits is not None:
    st.header("Credits per gebruiker")
    user_bal = credits.groupby("user")["balance"].last()
    st.bar_chart(user_bal)
