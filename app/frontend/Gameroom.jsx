import React, { useState } from "react";
import { useGame } from "./GameContext";

export default function Gameroom() {
  const { user, aiChat, aiFeedback, loading } = useGame();
  const [choice, setChoice] = useState("");
  const [msg, setMsg] = useState("");

  function handleChoice(opt) {
    setChoice(opt);
    setMsg("");
  }

  async function handleAskAI() {
    if (!user) return setMsg("Log eerst in!");
    await aiChat({ player_id: user.player_id, message: `Wat is de beste zet?` });
  }

  function handleConfirm() {
    setMsg(`Keuze bevestigd: ${choice}`);
  }

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-black bg-opacity-80 rounded-xl shadow-lg text-white">
      <div className="mb-4">
        <span className="text-lg font-semibold">🔁 Challenge #12 (Tijd: 30s)</span>
      </div>
      <div className="mb-4">
        <p className="font-medium">🔤 Vraag:</p>
        <p className="mb-2">Wat is de beste zet?</p>
      </div>
      <div className="space-y-2 mb-4">
        {["A", "B", "C"].map(opt => (
          <button
            key={opt}
            className={`w-full py-2 rounded transition ${choice === opt ? "bg-purple-800" : "bg-purple-700 hover:bg-purple-800"}`}
            onClick={() => handleChoice(opt)}
          >
            Optie {opt}
          </button>
        ))}
      </div>
      <div className="flex space-x-2">
        <button
          className="flex-1 py-2 rounded bg-green-700 hover:bg-green-800 transition"
          onClick={handleAskAI}
          disabled={loading}
        >
          💬 Vraag hulp aan AI 🤖
        </button>
        <button
          className="flex-1 py-2 rounded bg-indigo-700 hover:bg-indigo-800 transition"
          onClick={handleConfirm}
        >
          ✅ Bevestig keuze
        </button>
      </div>
      {aiFeedback && <div className="mt-4 text-blue-300">AI: {aiFeedback}</div>}
      {msg && <div className="mt-2 text-green-400">{msg}</div>}
    </div>
  );
}
