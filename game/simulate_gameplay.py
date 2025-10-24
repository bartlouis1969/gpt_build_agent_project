"""
simulate_gameplay.py

Simuleert een spelsessie en stuurt testdata naar game_feedback_loop.py.
Toont hoe de EA/selfhealing agent leert van gameplay.

Gebruik:
    python simulate_gameplay.py
"""

import json
import os
import random

from game_feedback_loop import process_game_event, process_game_outcome

AGENTS = ["AgentFury", "MindStrike", "QuantumOps"]
MISSIONS = ["Decode Sabotage", "Find Hidden Signal", "Optimize Portfolio"]
STRATEGIES = ["Aggressive", "Defensive", "Balanced"]

# Simuleer 5 events
for _ in range(5):
    event = {
        "player": random.choice(AGENTS),
        "mission": random.choice(MISSIONS),
        "action": random.choice(["buy", "sell", "hold", "get_hint"]),
        "context": {
            "market_volatility": round(random.uniform(0.1, 1.0), 2),
            "risk_level": random.choice(["low", "medium", "high"]),
        },
        "result": random.choice(["success", "fail", "retry"]),
    }
    process_game_event(event)
    print(f"Event logged: {event}")

# Simuleer een outcome
outcome = {
    "player": random.choice(AGENTS),
    "mission": random.choice(MISSIONS),
    "strategy": random.choice(STRATEGIES),
    "score": random.randint(50, 200),
    "success": random.choice([True, False]),
    "details": {
        "drawdown": round(random.uniform(0, 0.2), 2),
        "trades": random.randint(1, 10),
    },
}
process_game_outcome(outcome)
print(f"Outcome logged: {outcome}")

# Toon wat er in lessons.json staat
LESSONS_PATH = os.path.join(os.path.dirname(__file__), "..", "selfhealing", "lessons.json")
if os.path.exists(LESSONS_PATH):
    with open(LESSONS_PATH, encoding="utf-8") as f:
        lessons = json.load(f)
    print("\nEA Lessons:")
    for lesson in lessons[-3:]:
        print(lesson)

# Toon wat er in lessons.json staat
LESSONS_PATH = os.path.join(os.path.dirname(__file__), "..", "selfhealing", "lessons.json")
if os.path.exists(LESSONS_PATH):
    with open(LESSONS_PATH, encoding="utf-8") as f:
        lessons = json.load(f)
    print("\nEA Lessons:")
    for lesson in lessons[-3:]:
        print(lesson)
