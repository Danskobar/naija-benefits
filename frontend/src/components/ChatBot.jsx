import { useState, useRef, useEffect } from "react";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const QUICK_QUESTIONS = {
  english: [
    "I'm a young graduate looking for jobs",
    "I'm a pregnant woman needing health support",
    "I'm a farmer needing financial help",
    "I'm a student looking for scholarships",
    "I have a small business and need a loan",
    "I have a disability and need support",
  ],
  pidgin: [
    "I be fresh graduate wey dey find work",
    "I dey pregnant, I need health support",
    "I be farmer wey need money help",
    "I be student wey dey find scholarship",
    "I get small business, I need loan",
    "I get disability, I need support",
  ]
};

export default function ChatBot({ language }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [started, setStarted] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const startChat = async () => {
    setStarted(true);
    setLoading(true);
    try {
      const greeting = language === "pidgin"
        ? "Hello! How you dey?"
        : "Hello! I'd like to find benefits I qualify for.";

      const res = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: greeting, language, history: [] })
      });
      const data = await res.json();
      setMessages([
        { role: "user", content: greeting, hidden: true },
        { role: "assistant", content: data.reply }
      ]);
    } catch {
      setMessages([{
        role: "assistant",
        content: language === "pidgin"
          ? "E get problem with connection. Try again abeg!"
          : "Connection error. Please try again!"
      }]);
    }
    setLoading(false);
  };

  const sendMessage = async (text) => {
    const msg = text || input.trim();
    if (!msg || loading) return;
    setInput("");

    const newMessages = [...messages.filter(m => !m.hidden), { role: "user", content: msg }];
    setMessages(newMessages);
    setLoading(true);

    try {
      const history = newMessages.slice(0, -1).map(m => ({
        role: m.role,
        content: m.content
      }));

      const res = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg, language, history })
      });
      const data = await res.json();
      setMessages([...newMessages, { role: "assistant", content: data.reply }]);
    } catch {
      setMessages([...newMessages, {
        role: "assistant",
        content: language === "pidgin"
          ? "E get problem o! Try again abeg."
          : "Something went wrong. Please try again."
      }]);
    }
    setLoading(false);
  };

  if (!started) {
    return (
      <div className="chat-start">
        <div className="chat-start-card">
          <div className="chat-icon">🤖</div>
          <h2>{language === "pidgin" ? "NaijaBenefits AI dey here!" : "Welcome to NaijaBenefits AI"}</h2>
          <p>
            {language === "pidgin"
              ? "Tell me about yourself and I go find all government programs wey you qualify for — for free!"
              : "Tell me about your situation and I'll find all government benefits, scholarships, and programs you qualify for — completely free!"}
          </p>
          <button className="btn-start" onClick={startChat}>
            {language === "pidgin" ? "Start Talk 🚀" : "Start Chat 🚀"}
          </button>

          <div className="quick-examples">
            <p>{language === "pidgin" ? "Common questions:" : "Common questions:"}</p>
            <div className="examples-grid">
              {QUICK_QUESTIONS[language].map((q, i) => (
                <button key={i} className="example-btn" onClick={() => { setStarted(true); sendMessage(q); }}>
                  {q}
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="chatbot">
      <div className="messages">
        {messages.filter(m => !m.hidden).map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            {msg.role === "assistant" && <div className="avatar">🤖</div>}
            <div className="bubble">
              {msg.content.split('\n').map((line, j) => (
                <p key={j}>{line}</p>
              ))}
            </div>
            {msg.role === "user" && <div className="avatar user-avatar">👤</div>}
          </div>
        ))}
        {loading && (
          <div className="message assistant">
            <div className="avatar">🤖</div>
            <div className="bubble typing">
              <span></span><span></span><span></span>
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <div className="quick-replies">
        {QUICK_QUESTIONS[language].slice(0, 3).map((q, i) => (
          <button key={i} className="quick-reply" onClick={() => sendMessage(q)}>
            {q}
          </button>
        ))}
      </div>

      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === "Enter" && sendMessage()}
          placeholder={language === "pidgin" ? "Type your message here..." : "Type your message here..."}
          className="chat-input"
          disabled={loading}
        />
        <button className="btn-send" onClick={() => sendMessage()} disabled={loading || !input.trim()}>
          ➤
        </button>
      </div>
    </div>
  );
}
