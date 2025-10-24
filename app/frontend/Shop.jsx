import React from "react";
import { useGame } from "./GameContext";

export default function Shop() {
  const { user, updateCredits, loading } = useGame();

  function handleBuy(amount) {
    if (!user) return;
    updateCredits({ player_id: user.player_id, amount: -amount, action: "spend" });
  }

  return (
    <div className="max-w-xs mx-auto mt-10 p-4 bg-black bg-opacity-80 rounded-xl shadow text-white">
      <h2 className="text-xl font-bold mb-2">🎁 Winkel</h2>
      <div className="space-y-2">
        <div className="flex justify-between items-center bg-gray-900 p-2 rounded">
          <span>🔓 Extra leven</span>
          <button className="font-mono bg-green-700 px-2 py-1 rounded" onClick={() => handleBuy(100)} disabled={loading}>100¢</button>
        </div>
        <div className="flex justify-between items-center bg-gray-900 p-2 rounded">
          <span>💡 Hint kaart</span>
          <button className="font-mono bg-green-700 px-2 py-1 rounded" onClick={() => handleBuy(50)} disabled={loading}>50¢</button>
        </div>
        <div className="flex justify-between items-center bg-gray-900 p-2 rounded">
          <span>🎨 Skin pakket</span>
          <button className="font-mono bg-green-700 px-2 py-1 rounded" onClick={() => handleBuy(300)} disabled={loading}>300¢</button>
        </div>
      </div>
    </div>
  );
}
