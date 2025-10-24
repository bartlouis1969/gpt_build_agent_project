# Dummy MT5 connector for demo/live trading integration
# In productie: gebruik MetaTrader5 package of broker API


class MT5Connector:
    def __init__(self, account_type="demo"):
        self.account_type = account_type
        self.connected = False

    def connect(self):
        # Simuleer verbinding
        self.connected = True
        return True

    def place_trade(self, symbol, lot_size, stop_loss, risk):
        # Simuleer trade-plaatsing
        return {
            "status": "ok",
            "symbol": symbol,
            "lot_size": lot_size,
            "stop_loss": stop_loss,
            "risk": risk,
            "account_type": self.account_type,
            "trade_id": "T123456",
        }

    def disconnect(self):
        self.connected = False
        return True
