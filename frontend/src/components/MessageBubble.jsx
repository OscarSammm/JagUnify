// Renders bot answer text with bold, line breaks, and clickable citation links
function renderBotText(text, sources) {
  return text.split("\n").map((line, lineIdx, arr) => {
    const parts = line.split(/(\*\*[^*]+\*\*|\[\d+\])/g);

    const rendered = parts.map((part, partIdx) => {
      const boldMatch = part.match(/^\*\*([^*]+)\*\*$/);
      if (boldMatch) return <strong key={partIdx}>{boldMatch[1]}</strong>;

      const citeMatch = part.match(/^\[(\d+)\]$/);
      if (citeMatch) {
        const id = parseInt(citeMatch[1]);
        const source = sources?.find((s) => s.id === id);
        if (source) {
          return (
            <a
              key={partIdx}
              href={source.url}
              target="_blank"
              rel="noreferrer"
              className="font-semibold text-amber-200 hover:underline"
            >
              [{id}]
            </a>
          );
        }
      }

      return part;
    });

    return (
      <span key={lineIdx}>
        {rendered}
        {lineIdx < arr.length - 1 && <br />}
      </span>
    );
  });
}

export default function MessageBubble({ message }) {
  const isHuman = message.role === "human";

  return (
    <>
      <div
        className={[
          "mt-2 mb-2 w-fit max-w-[45%] rounded-xl border border-zinc-300 px-3 py-2 text-white",
          isHuman
            ? "mr-4 self-end bg-[#6b2f3cab]"
            : "ml-4 self-start bg-[#6b2f3cab]",
        ].join(" ")}
      >
        {isHuman ? (
          message.text
        ) : (
          <>
            {renderBotText(message.text, message.sources)}

            {/* Sources list */}
            {message.sources && message.sources.length > 0 && (
              <div className="mt-3 border-t border-white/20 pt-2 text-xs text-blue-200">
                {message.sources.map((src) => (
                  <div key={src.id} className="group relative">
                    [{src.id}]{" "}
                    <a
                      href={src.url}
                      target="_blank"
                      rel="noreferrer"
                      className="underline hover:text-blue-400"
                    >
                      {src.url}
                    </a>
                    <div className="pointer-events-none absolute left-0 top-full z-50 mt-1 hidden w-80 rounded-lg border border-zinc-300 bg-white p-3 text-xs text-zinc-800 shadow-lg group-hover:block">
                      <div className="mb-1 font-semibold text-zinc-900">
                        Source preview
                      </div>
                      <div>{src.snippet || "No preview available."}</div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </>
        )}
      </div>

      <div
        className={[
          "text-xs text-zinc-700",
          isHuman ? "mr-6 self-end" : "ml-6 self-start",
        ].join(" ")}
      >
        {message.time}
      </div>
    </>
  );
}
