import React, { useState } from "react";
import { useGame } from "./GameContext";

export default function TradeSetupForm() {
  const { user, tradingSetup, tradeResult, loading } = useGame();
  const [form, setForm] = useState({
    symbol: "EURUSD",
    risk: 1,
    lot_size: 0.01,
    stop_loss: 20,
    account_type: "demo",
  });
  const [msg, setMsg] = useState("");

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }
  async function handleSubmit(e) {
    e.preventDefault();
    if (!user) return setMsg("Log eerst in!");
    setMsg("");
    const res = await tradingSetup({ player_id: user.player_id, ...form });
    setMsg(res.status === "ok" ? "Trade geplaatst!" : "Fout bij trade");
  }
  return (
    <form onSubmit={handleSubmit} className="space-y-4 bg-black bg-opacity-80 p-4 rounded-xl shadow text-white">
      <div>
        <label className="block mb-1">Trading Pair</label>
        <input name="symbol" value={form.symbol} onChange={handleChange} className="w-full p-2 rounded bg-gray-900" />
      </div>
      <div>
        <label className="block mb-1">Risk %</label>
        <input name="risk" type="number" min="0.1" max="10" step="0.1" value={form.risk} onChange={handleChange} className="w-full p-2 rounded bg-gray-900" />
      </div>
      <div>
        <label className="block mb-1">Lot Size</label>
        <input name="lot_size" type="number" min="0.01" step="0.01" value={form.lot_size} onChange={handleChange} className="w-full p-2 rounded bg-gray-900" />
      </div>
      <div>
        <label className="block mb-1">Stop Loss (pips)</label>
        <input name="stop_loss" type="number" min="1" value={form.stop_loss} onChange={handleChange} className="w-full p-2 rounded bg-gray-900" />
      </div>
      <div>
        <label className="block mb-1">Account Type</label>
        <select name="account_type" value={form.account_type} onChange={handleChange} className="w-full p-2 rounded bg-gray-900">
          <option value="demo">Demo</option>
          <option value="real">Live</option>
        </select>
      </div>
      <button type="submit" className="w-full py-2 rounded bg-green-700 hover:bg-green-800 transition" disabled={loading}>
        {loading ? "Bezig..." : "Verstuur setup"}
      </button>
      {msg && <div className="text-green-400 mt-2">{msg}</div>}
      {tradeResult && (
        <div className="text-blue-300 mt-2">Trade ID: {tradeResult.trade_id} ({tradeResult.status})</div>
      )}
    </form>
  );
}
