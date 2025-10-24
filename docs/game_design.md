# AI.RING Evolutionair Tradingplatform — Architectuur & Logica

---

## 🧠 EA, Spel & Speler: Synergie

### 1. EA leert van spelers

- Spelers zijn datasources: keuzes, strategieën, win/verlies worden gelogd
- EA analyseert logs (`game_feedback_loop.py`):
  - Herkent patronen
  - Detecteert succesvolle strategieën
  - Past signalen aan op basis van beste spelers

### 2. Spelers profiteren van EA

- Demo: EA coacht, corrigeert, beschermt
- Live: EA stuurt signalen, beschermt kapitaal, personaliseert stijl

### 3. Demo vs. Live

| Aspect      | Demo Mode | Live Mode |
| ----------- | --------- | --------- |
| Accounttype | Simulatie | MT5 real/funded |
| Bescherming | Volledige coaching | Waakzaam, gebruiker beslist |
| Datawaarde  | EA-training | Logging & alerts |
| Risico      | Geen | Echt kapitaal, FTMO-bescherming |

### 4. Unieke trades per speler/account

- Instellingen, profiel, AI-adaptatie → unieke live trades
- lessons.json groeit per speler

---

## 🔒 FTMO-regelbescherming

- Drawdown-limieten
- Risicoper trade
- Max actieve posities
- EA grijpt in: trade weigeren/beperken/uitschakelen

---

## 🔄 AI-keuringsmodel

- Score >73% = live/funded
- Score 50-73% = beperkt demo/live
- Score <50% = alleen demo

---

## 🔗 Copy My Results

- Spelers kunnen live signalen delen/volgen
- Premium-signalen, profit split, affiliate

---

## 📦 Systeemcomponenten

- `ea_config.py`: keuringsregels, triggers, accountstatus, FTMO-compliance
- `mt5_connector.py`: demo/live accountbeheer
- `backend/routes/player_settings.py`: copy signal toggle, accounttype, gedrag
- Geavanceerd logging & scoring per strategie

---

## 💡 Waarom spelers betalen

- Leren door te spelen
- Verdienen door te leren
- Coach/signal-provider worden
- AI-coach, live signalen, veilige MT5, game-progressie

---

## 📌 Implementatie

- Zie `ea_config.py`, `mt5_connector.py`, `player_settings.py` voor technische details
