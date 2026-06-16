import { useState } from "react";
import ChatBot from "./components/ChatBot";
import BrowsePrograms from "./components/BrowsePrograms";
import Header from "./components/Header";
import Hero from "./components/Hero";
import "./App.css";

export default function App() {
  const [tab, setTab] = useState("chat");
  const [language, setLanguage] = useState("english");

  return (
    <div className="app">
      <Header language={language} setLanguage={setLanguage} />
      <Hero />

      <div className="tabs">
        <button className={tab === "chat" ? "active" : ""} onClick={() => setTab("chat")}>
          🤖 AI Assistant
        </button>
        <button className={tab === "browse" ? "active" : ""} onClick={() => setTab("browse")}>
          📋 Browse Programs
        </button>
      </div>

      <main className="main">
        {tab === "chat" && <ChatBot language={language} />}
        {tab === "browse" && <BrowsePrograms />}
      </main>

      <footer className="footer">
        <p>NaijaBenefits AI — Built for USAII Global AI Hackathon 2026</p>
        <p>Helping Nigerians access the support they deserve 🇳🇬</p>
      </footer>
    </div>
  );
}