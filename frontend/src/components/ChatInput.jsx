export default function ChatInput({
  inputRef,
  input,
  setInput,
  isWaiting,
  sendMessage,
}) {
  return (
    <div className="mx-auto mt-4 mb-20 flex w-full max-w-5xl items-end justify-center gap-3">
      <textarea
        ref={inputRef}
        value={input}
        disabled={isWaiting}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
          }
        }}
        placeholder={
          isWaiting ? "Waiting for response..." : "Type in your question ..."
        }
        className="min-h-[64px] w-full resize-none rounded-xl border-2 border-zinc-300 bg-white px-3 py-2 text-lg outline-none transition focus:border-zinc-500 disabled:cursor-not-allowed disabled:bg-zinc-400 disabled:text-black disabled:opacity-100
        disabled:cursor-not-allowed
        disabled:bg-zinc-300
        disabled:text-zinc-500
        disabled:opacity-70"
      />
      <button
        onClick={sendMessage}
        title="Send message"
        disabled={isWaiting}
        className="flex h-[75px] w-[70px] shrink-0 items-center justify-center rounded-xl border border-zinc-300 bg-[#6b2f3c] shadow disabled:opacity-70"
      >
        <img
          src="/img/jag-send.png"
          alt="send"
          className="h-25 w-100 object-contain"
        />
      </button>
      <button
        onClick={() => window.location.reload()}
        title="Delete chat history"
        className="flex h-[75px] w-[70px] items-center justify-center rounded-xl border border-zinc-300 bg-[#6b2f3c] shadow hover:opacity-90"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="22"
          height="22"
          fill="currentColor"
          className="text-orange-400"
          viewBox="0 0 16 16"
        >
          <path d="M8 16c3.314 0 6-2 6-5.5 0-1.5-.5-4-2.5-6 .25 1.5-1.25 2-1.25 2C11 4 9 .5 6 0c.357 2 .5 4-2 6-1.25 1-2 2.729-2 4.5C2 14 4.686 16 8 16m0-1c-1.657 0-3-1-3-2.75 0-.75.25-2 1.25-3C6.125 10 7 10.5 7 10.5c-.375-1.25.5-3.25 2-3.5-.179 1-.25 2 1 3 .625.5 1 1.364 1 2.25C11 14 9.657 15 8 15" />
        </svg>
      </button>
    </div>
  );
}
