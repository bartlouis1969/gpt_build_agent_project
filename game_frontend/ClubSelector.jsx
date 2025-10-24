import React, { useState } from 'react';

const clubs = ["AlphaVerse", "SentienceCore", "MindGuild", "QuantumOps"];

export default function ClubSelector() {
  const [selected, setSelected] = useState(clubs[0]);

  return (
    <div className="max-w-sm mx-auto mt-8 p-4 bg-white rounded shadow">
      <h2 className="text-xl font-bold mb-4">Kies je club</h2>
      <select
        className="w-full p-2 border rounded mb-4"
        value={selected}
        onChange={e => setSelected(e.target.value)}
      >
        {clubs.map(club => (
          <option key={club} value={club}>{club}</option>
        ))}
      </select>
      <div className="text-gray-700">Geselecteerd: <span className="font-semibold">{selected}</span></div>
    </div>
  );
}
