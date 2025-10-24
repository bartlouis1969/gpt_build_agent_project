"""
EA-configuratie: keuringsregels, triggers, accountstatus, FTMO-compliance
"""


class EAConfig:
    def __init__(self):
        self.approval_threshold = 0.73  # 73% goedkeuringsscore
        self.ftmo_limits = {
            "daily_drawdown": 0.05,  # 5%
            "overall_drawdown": 0.10,  # 10%
            "max_risk_per_trade": 0.02,  # 2%
            "max_active_positions": 5,
        }

    def approve_strategy(self, score):
        if score >= self.approval_threshold:
            return "live"
        elif score >= 0.5:
            return "demo"
        else:
            return "test"

    def check_ftmo_compliance(self, account, trade):
        # account: dict met saldo, open trades, drawdown
        # trade: dict met risk, size, etc.
        if account["daily_drawdown"] > self.ftmo_limits["daily_drawdown"]:
            return False, "Daily drawdown limit exceeded"
        if account["overall_drawdown"] > self.ftmo_limits["overall_drawdown"]:
            return False, "Overall drawdown limit exceeded"
        if trade["risk"] > self.ftmo_limits["max_risk_per_trade"]:
            return False, "Risk per trade too high"
        if account["active_positions"] > self.ftmo_limits["max_active_positions"]:
            return False, "Too many active positions"
        return True, "Compliant"

    def get_account_status(self, player_id):
        # Dummy: return demo/live/funded
        # In productie: lookup in DB
        return "demo"

    def log_strategy(self, player_id, strategy, score):
        # Log strategie, score, accounttype
        pass
