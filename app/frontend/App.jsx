import React from "react";
import { GameProvider } from "./GameContext";
import HomeLogin from "./HomeLogin";
import Gameroom from "./Gameroom";
import AIChat from "./AIChat";
import ScoreCredits from "./ScoreCredits";
import Clubroom from "./Clubroom";
import Shop from "./Shop";
import TradingViewWidget from "./TradingViewWidget";
import TradeSetupForm from "./TradeSetupForm";

export default function App() {
  return (
    <GameProvider>
      <div className="min-h-screen bg-gradient-to-br from-black via-purple-900 to-blue-900 p-4">
        {/* Voorbeeld: HomeLogin, Gameroom, Trading, etc. */}
        <div className="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
          <div>
            <HomeLogin />
            <Gameroom />
            <ScoreCredits />
            <Shop />
          </div>
          <div>
            <TradingViewWidget symbol="EURUSD" />
            <TradeSetupForm onSubmit={console.log} />
            <AIChat />
            <Clubroom />
          </div>
        </div>
      </div>
    </GameProvider>
  );
}
