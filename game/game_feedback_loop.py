"""
Utilities voor het feedback-loopje in de game.

Dit module verzamelt speler-events, berekent eenvoudige scores en
formatteert een korte suggestie voor de volgende actie.
"""

import json
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
LESSONS_PATH = os.path.join(os.path.dirname(__file__), "..", "selfhealing", "lessons.json")
EVENT_LOG = os.path.join(DATA_DIR, "event_log.json")
GAME_OUTCOME = os.path.join(DATA_DIR, "game_outcome.json")

os.makedirs(DATA_DIR, exist_ok=True)


def process_game_event(event):
    """Log een individuele spelactie naar event_log.json"""
    event["timestamp"] = datetime.utcnow().isoformat()
    try:
        with open(EVENT_LOG, encoding="utf-8") as f:
            events = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        events = []
    events.append(event)
    with open(EVENT_LOG, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2)


def process_game_outcome(outcome):
    """Log een gamesessie-uitkomst en update lessons.json"""
    outcome["timestamp"] = datetime.utcnow().isoformat()
    try:
        with open(GAME_OUTCOME, encoding="utf-8") as f:
            outcomes = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        outcomes = []
    outcomes.append(outcome)
    with open(GAME_OUTCOME, "w", encoding="utf-8") as f:
        json.dump(outcomes, f, indent=2)
    # Update lessons.json
    lesson = {
        "strategy": outcome.get("strategy"),
        "score": outcome.get("score"),
        "success": outcome.get("success"),
        "details": outcome.get("details"),
        "timestamp": outcome["timestamp"],
    }
    try:
        with open(LESSONS_PATH, encoding="utf-8") as f:
            lessons = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        lessons = []
    lessons.append(lesson)
    with open(LESSONS_PATH, "w", encoding="utf-8") as f:
        json.dump(lessons, f, indent=2)
