export default function Header({ language, setLanguage }) {
  return (
    <header className="header">
      <div className="header-logo">
        <span className="logo-flag">🇳🇬</span>
        <div>
          <span className="logo-text">NaijaBenefits <strong>AI</strong></span>
          <span className="logo-sub">Find Your Government Benefits</span>
        </div>
      </div>
      <div className="header-right">
        <div className="lang-toggle">
          <button
            className={language === "english" ? "active" : ""}
            onClick={() => setLanguage("english")}
          >
            English
          </button>
          <button
            className={language === "pidgin" ? "active" : ""}
            onClick={() => setLanguage("pidgin")}
          >
            Pidgin
          </button>
        </div>
      </div>
    </header>
  );
}
