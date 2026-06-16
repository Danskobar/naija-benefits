import { useState, useEffect } from "react";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const CATEGORY_ICONS = {
  employment: "💼",
  business: "🏪",
  education: "🎓",
  health: "🏥",
  welfare: "🤝",
  agriculture: "🌾",
  housing: "🏠",
  youth: "👨‍💼",
  disability: "♿"
};

export default function BrowsePrograms() {
  const [benefits, setBenefits] = useState([]);
  const [filtered, setFiltered] = useState([]);
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("all");
  const [selected, setSelected] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API_URL}/benefits`)
      .then(r => r.json())
      .then(d => {
        setBenefits(d.benefits);
        setFiltered(d.benefits);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  useEffect(() => {
    let results = benefits;
    if (category !== "all") {
      results = results.filter(b => b.category === category);
    }
    if (search) {
      const q = search.toLowerCase();
      results = results.filter(b =>
        b.name.toLowerCase().includes(q) ||
        b.description.toLowerCase().includes(q) ||
        b.tags.some(t => t.includes(q))
      );
    }
    setFiltered(results);
  }, [search, category, benefits]);

  const categories = ["all", ...new Set(benefits.map(b => b.category))];

  if (selected) {
    return (
      <div className="program-detail">
        <button className="btn-back" onClick={() => setSelected(null)}>← Back to Programs</button>
        <div className="detail-card">
          <div className="detail-header">
            <span className="detail-icon">{CATEGORY_ICONS[selected.category]}</span>
            <div>
              <h2>{selected.name}</h2>
              <span className="category-tag">{selected.category}</span>
            </div>
          </div>
          <p className="detail-desc">{selected.description}</p>

          <div className="detail-amount">
            💰 {selected.benefit_amount}
          </div>

          <div className="detail-section">
            <h3>✅ Who Can Apply</h3>
            <ul>
              {selected.eligibility.map((e, i) => <li key={i}>{e}</li>)}
            </ul>
          </div>

          <div className="detail-section">
            <h3>📝 How to Apply</h3>
            <p>{selected.how_to_apply}</p>
          </div>

          <div className="detail-section">
            <h3>📅 Deadline</h3>
            <p>{selected.deadline}</p>
          </div>

          <div className="detail-section">
            <h3>🏛️ Ministry/Agency</h3>
            <p>{selected.ministry}</p>
          </div>

          <a href={selected.website} target="_blank" rel="noreferrer" className="btn-apply">
            Apply Now → {selected.website}
          </a>
        </div>
      </div>
    );
  }

  return (
    <div className="browse">
      <div className="browse-header">
        <h2>All Nigerian Government Programs</h2>
        <p>Browse {benefits.length} benefits, scholarships, and support programs</p>
      </div>

      <div className="search-bar">
        <input
          type="text"
          placeholder="🔍 Search programs (e.g. scholarship, loan, health...)"
          value={search}
          onChange={e => setSearch(e.target.value)}
          className="search-input"
        />
      </div>

      <div className="category-filters">
        {categories.map(cat => (
          <button
            key={cat}
            className={`cat-btn ${category === cat ? "active" : ""}`}
            onClick={() => setCategory(cat)}
          >
            {cat === "all" ? "🇳🇬 All" : `${CATEGORY_ICONS[cat]} ${cat}`}
          </button>
        ))}
      </div>

      {loading ? (
        <div className="loading">Loading programs...</div>
      ) : (
        <div className="programs-grid">
          {filtered.map(benefit => (
            <div key={benefit.id} className="program-card" onClick={() => setSelected(benefit)}>
              <div className="program-card-header">
                <span className="program-icon">{CATEGORY_ICONS[benefit.category]}</span>
                <span className="program-category">{benefit.category}</span>
              </div>
              <h3>{benefit.name}</h3>
              <p>{benefit.description.slice(0, 100)}...</p>
              <div className="program-amount">💰 {benefit.benefit_amount}</div>
              <button className="btn-details">View Details →</button>
            </div>
          ))}
          {filtered.length === 0 && (
            <div className="no-results">No programs found. Try a different search.</div>
          )}
        </div>
      )}
    </div>
  );
}
