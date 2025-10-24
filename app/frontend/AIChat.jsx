import React, { useState } from "react";
import { useGame } from "./GameContext";

export default function AIChat() {
  const { user, aiChat, aiFeedback, loading } = useGame();
  const [input, setInput] = useState("");
  const [history, setHistory] = useState([]);

  async function handleSend(e) {
    e.preventDefault();
    if (!user) return;
    const res = await aiChat({ player_id: user.player_id, message: input });
    setHistory([...history, { role: "user", text: input }, { role: "ai", text: res.response }]);
    setInput("");
  }

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-gradient-to-br from-black via-purple-900 to-blue-900 rounded-xl shadow-lg text-white">
      <div className="mb-4">
        <span className="text-lg font-semibold">🤖 GPT zegt:</span>
      </div>
      <div className="mb-4 max-h-40 overflow-y-auto">
        {history.map((msg, i) => (
          <div key={i} className={msg.role === "user" ? "text-right" : "text-left text-blue-300"}>
            <span className="font-medium">{msg.role === "user" ? "🧑 Jij:" : "🤖 GPT:"}</span> {msg.text}
          </div>
        ))}
        {aiFeedback && <div className="text-blue-300">AI: {aiFeedback}</div>}
      </div>
      <form onSubmit={handleSend} className="flex space-x-2">
        <input
          className="flex-1 p-2 rounded bg-gray-900"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Stel een vraag aan de AI..."
        />
        <button type="submit" className="py-2 px-4 rounded bg-green-700 hover:bg-green-800 transition" disabled={loading}>
          Verstuur
        </button>
      </form>
    </div>
  );
}
