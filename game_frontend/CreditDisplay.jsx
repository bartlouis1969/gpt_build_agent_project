import React from 'react';

export default function CreditDisplay({ credits = 120 }) {
  return (
    <div className="inline-flex items-center px-3 py-1 bg-yellow-100 rounded-full shadow text-yellow-800 font-bold">
      <svg className="w-5 h-5 mr-2 text-yellow-500" fill="currentColor" viewBox="0 0 20 20"><circle cx="10" cy="10" r="8" /></svg>
      {credits} Credits
    </div>
  );
}
