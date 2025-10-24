import React from 'react';

export default function GameScreen({ agentName = "AgentFury", credits = 120, mission = "Decode Sabotage" }) {
  return (
    <div className="max-w-lg mx-auto mt-8 p-6 bg-gray-50 rounded shadow">
      <h2 className="text-2xl font-bold mb-2">Mission: {mission}</h2>
      <div className="mb-4">AI-Agent: <span className="font-semibold">{agentName}</span></div>
      <div className="mb-2">Credits: <span className="font-bold">{credits}</span></div>
      <div className="mb-4">Progress: <span className="text-green-600">40%</span></div>
      <button className="bg-green-600 text-white px-4 py-2 rounded mr-2">Submit Answer</button>
      <button className="bg-blue-500 text-white px-4 py-2 rounded">Get Hint</button>
    </div>
  );
}
