import React, { useEffect, useRef } from "react";

export default function TradingViewWidget({ symbol = "EURUSD" }) {
  const container = useRef(null);
  useEffect(() => {
    if (window.TradingView) return;
    const script = document.createElement("script");
    script.src = "https://s3.tradingview.com/tv.js";
    script.async = true;
    script.onload = () => {
      if (window.TradingView && container.current) {
        new window.TradingView.widget({
          autosize: true,
          symbol: symbol,
          interval: "15",
          timezone: "Europe/Amsterdam",
          theme: "dark",
          style: "1",
          locale: "en",
          container_id: container.current.id,
        });
      }
    };
    document.body.appendChild(script);
  }, [symbol]);
  return (
    <div className="rounded-xl overflow-hidden shadow-lg border border-gray-800 bg-black">
      <div id="tradingview-widget" ref={container} style={{ height: 400, minWidth: 320 }} />
    </div>
  );
}
