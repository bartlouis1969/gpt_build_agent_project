import React, { createContext, useContext, useState } from "react";

const GameContext = createContext();

export function GameProvider({ children }) {
  const [user, setUser] = useState(null); // {player_id, token}
  const [credits, setCredits] = useState(0);
  const [aiFeedback, setAiFeedback] = useState("");
  const [tradeResult, setTradeResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // API helpers
  async function login({ email, player_name }) {
    setLoading(true);
    const res = await fetch("/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, player_name }),
    });
    const data = await res.json();
    setUser({ player_id: data.player_id, token: data.token });
    setLoading(false);
    return data;
  }

  async function fetchCredits(player_id) {
    setLoading(true);
    const res = await fetch(`/api/credits?player_id=${player_id}`);
    const data = await res.json();
    setCredits(data.credits);
    setLoading(false);
    return data;
  }

  async function updateCredits(payload) {
    setLoading(true);
    const res = await fetch("/api/credits/update", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    setCredits(data.new_credits);
    setLoading(false);
    return data;
  }

  async function aiChat(payload) {
    setLoading(true);
    const res = await fetch("/api/ai/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    setAiFeedback(data.response);
    setLoading(false);
    return data;
  }

  async function tradingSetup(payload) {
    setLoading(true);
    const res = await fetch("/api/game/trading-setup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    setTradeResult(data.trade_result);
    setLoading(false);
    return data;
  }

  return (
    <GameContext.Provider
      value={{
        user,
        setUser,
        credits,
        setCredits,
        aiFeedback,
        setAiFeedback,
        tradeResult,
        setTradeResult,
        loading,
        login,
        fetchCredits,
        updateCredits,
        aiChat,
        tradingSetup,
      }}
    >
      {children}
    </GameContext.Provider>
  );
}

export function useGame() {
  return useContext(GameContext);
}
