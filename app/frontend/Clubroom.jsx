import React from "react";

export default function Clubroom() {
  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-black bg-opacity-80 rounded-xl shadow-lg text-white">
      <h2 className="text-2xl font-bold mb-2">🏰 Club: "QuantumKings"</h2>
      <div className="mb-4">
        <div className="mb-2">🗣️ Chat met leden</div>
        <div className="bg-gray-900 p-2 rounded mb-2">"Nice job op challenge 7!"</div>
      </div>
      <div className="flex justify-between">
        <div>👥 Leden: <span className="font-mono">8/12</span></div>
        <div>📈 Club-score: <span className="font-mono">16200</span></div>
      </div>
    </div>
  );
}
