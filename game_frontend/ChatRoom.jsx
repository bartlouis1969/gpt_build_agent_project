import React, { useState } from 'react';

export default function ChatRoom({ club = "AlphaVerse" }) {
  const [messages, setMessages] = useState([
    { user: "AgentFury", text: "Welkom in de club!" },
    { user: "MindStrike", text: "Wie doet mee aan de missie?" }
  ]);
  const [input, setInput] = useState('');

  const sendMessage = (e) => {
    e.preventDefault();
    if (input.trim()) {
      setMessages([...messages, { user: "Jij", text: input }]);
      setInput('');
    }
  };

  return (
    <div className="max-w-md mx-auto mt-8 p-4 bg-white rounded shadow">
      <h2 className="text-xl font-bold mb-2">Clubchat: {club}</h2>
      <div className="h-40 overflow-y-auto mb-2 border rounded p-2 bg-gray-50">
        {messages.map((msg, i) => (
          <div key={i} className="mb-1"><span className="font-semibold">{msg.user}:</span> {msg.text}</div>
        ))}
      </div>
      <form onSubmit={sendMessage} className="flex">
        <input
          type="text"
          className="flex-1 p-2 border rounded-l"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Typ een bericht..."
        />
        <button type="submit" className="bg-blue-600 text-white px-4 rounded-r">Send</button>
      </form>
    </div>
  );
}
