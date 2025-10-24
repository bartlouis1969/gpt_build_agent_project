import React, { useState } from "react";
import { useGame } from "./GameContext";

export default function HomeLogin() {
  const { user, login, loading } = useGame();
  const [email, setEmail] = useState("");
  const [playerName, setPlayerName] = useState("");
  const [msg, setMsg] = useState("");

  async function handleLogin(e) {
    e.preventDefault();
    setMsg("");
    const res = await login({ email, player_name: playerName });
    setMsg(res.player_id ? `Welkom, ${res.player_id}!` : "Login mislukt");
  }

  return (
    <div className="flex flex-col items-center justify-center text-white p-4">
      <h1 className="text-4xl font-bold mb-2">AI Club Clash</h1>
      <p className="mb-6">Welkom bij het spel</p>
      <form onSubmit={handleLogin} className="space-y-4 w-full max-w-xs">
        <input
          className="w-full p-2 rounded bg-gray-900"
          placeholder="E-mail (optioneel)"
          value={email}
          onChange={e => setEmail(e.target.value)}
        />
        <input
          className="w-full p-2 rounded bg-gray-900"
          placeholder="Spelernaam (optioneel)"
          value={playerName}
          onChange={e => setPlayerName(e.target.value)}
        />
        <button
          type="submit"
          className="w-full py-2 rounded bg-purple-700 hover:bg-purple-800 transition"
          disabled={loading}
        >
          {loading ? "Bezig..." : "Inloggen / Gast starten"}
        </button>
      </form>
      <p className="mt-4 text-xs text-gray-300">🔒 Clubs alleen met login</p>
      {msg && <div className="mt-2 text-green-400">{msg}</div>}
      {user && <div className="mt-2 text-blue-300">Ingelogd als: {user.player_id}</div>}
    </div>
  );
}
