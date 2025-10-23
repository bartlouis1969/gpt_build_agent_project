import os
import streamlit as st
import requests
from datetime import datetime
import json
import websockets
import asyncio

st.set_page_config(page_title="GPT Build Agent", layout="centered")

# --- Sidebar instellingen ---
st.sidebar.title("⚙️ Instellingen")
api_url = os.getenv("AGENT_API_URL") or st.sidebar.text_input(
    "API endpoint", value="http://localhost:8000/ai/generate"
)
api_token = st.sidebar.text_input("API-token", type="password")
model_choice = st.sidebar.selectbox("Model", ["GPT-4", "GPT-3.5"])

# --- Upload contextbestand ---
context_file = st.sidebar.file_uploader("Upload contextbestand (JSON)", type=["json"])
if context_file:
    context_data = json.load(context_file)
else:
    context_data = None

# --- Persistent geheugen ---
history_file = "chat_history.json"
if "history" not in st.session_state:
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as f:
            st.session_state.history = json.load(f)
    else:
        st.session_state.history = []

st.title("🤖 GPT Build Agent Chat")
st.caption("Stel een vraag aan je zelfverbeterende AI-agent")

# --- Herstart gesprek ---
if st.sidebar.button("🔄 Herstart gesprek"):
    st.session_state.history = []
    if os.path.exists(history_file):
        os.remove(history_file)
    st.success("Gesprek herstart")

# --- Toon gespreksgeschiedenis ---
for entry in reversed(st.session_state.history):
    st.markdown(f"**🧑 Jij:** {entry['user']}")
    st.markdown(f"**🤖 Agent:** {entry['agent']}")
    st.caption(f"🕒 {entry['timestamp']}")

# --- Promptformulier ---
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_area("Typ je prompt:", height=100)
    submitted = st.form_submit_button("Verstuur")

# --- API-call bij verzenden ---


async def fetch_streaming_response(api_url, payload, headers):
    async with websockets.connect(api_url.replace("http", "ws")) as ws:
        await ws.send(json.dumps(payload))
        response = ""
        while True:
            chunk = await ws.recv()
            if not chunk:
                break
            response += chunk
        return response


if submitted and user_input.strip():
    payload = {
        "prompt": user_input,
        "model": model_choice,
    }
    if context_data:
        payload["context"] = context_data
    headers = {"Authorization": f"Bearer {api_token}"} if api_token else {}
    try:
        # --- Websocket streaming ---
        if api_url.startswith("ws") or "/stream" in api_url:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            ai_output = loop.run_until_complete(
                fetch_streaming_response(api_url, payload, headers)
            )
        else:
            response = requests.post(api_url, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            ai_output = (
                response.json().get("result")
                or response.json().get("content")
                or "⚠️ Geen antwoord ontvangen."
            )

        st.session_state.history.append(
            {
                "user": user_input,
                "agent": ai_output,
                "timestamp": datetime.now().strftime("%H:%M:%S"),
            }
        )
        with open(history_file, "w", encoding="utf-8") as f:
            json.dump(st.session_state.history, f, ensure_ascii=False, indent=2)
        st.rerun()

    except Exception as e:
        st.error(f"❌ Fout bij verbinden met API: {e}")
