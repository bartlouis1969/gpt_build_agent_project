import React, { useEffect } from "react";
import { useGame } from "./GameContext";

export default function ScoreCredits() {
  const { user, credits, fetchCredits } = useGame();

  useEffect(() => {
    if (user) fetchCredits(user.player_id);
    // eslint-disable-next-line
  }, [user]);

  return (
    <div className="max-w-xs mx-auto mt-10 p-4 bg-black bg-opacity-80 rounded-xl shadow text-white">
      <h2 className="text-xl font-bold mb-2">🎯 Jouw score</h2>
      <div className="space-y-1">
        <div>💰 Credits: <span className="font-mono">{credits}</span></div>
      </div>
    </div>
  );
}
