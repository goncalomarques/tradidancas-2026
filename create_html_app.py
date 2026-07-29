import json
from generate_ics import events

# Generate HTML file
html_template = """<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TRADIDANÇAS 2026 - Programa Oficial</title>
  <meta name="description" content="Programa completo do festival Tradidanças 2026 (29 de Julho a 2 de Agosto). Oficinas, concertos, bailes, conversas e atividades.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #0f172a;
      --bg-card: rgba(30, 41, 59, 0.7);
      --bg-card-hover: rgba(51, 65, 85, 0.8);
      --primary: #f59e0b;
      --primary-light: #fbbf24;
      --accent: #ec4899;
      --accent-green: #10b981;
      --accent-blue: #3b82f6;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --border-color: rgba(255, 255, 255, 0.1);
      --glass-bg: rgba(15, 23, 42, 0.75);
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: var(--bg-dark);
      color: var(--text-main);
      min-height: 100vh;
      background-image: 
        radial-gradient(at 10% 10%, rgba(245, 158, 11, 0.15) 0px, transparent 50%),
        radial-gradient(at 90% 20%, rgba(236, 72, 153, 0.15) 0px, transparent 50%),
        radial-gradient(at 50% 90%, rgba(16, 185, 129, 0.15) 0px, transparent 50%);
      background-attachment: fixed;
      padding-bottom: 60px;
    }

    header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--glass-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-color);
      padding: 1.25rem 2rem;
    }

    .header-container {
      max-width: 1300px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .brand h1 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.8rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      background: linear-gradient(135deg, #f59e0b 0%, #ec4899 50%, #3b82f6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand .dates {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.05);
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      border: 1px solid var(--border-color);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .btn-download {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #0f172a;
      font-weight: 700;
      font-size: 0.9rem;
      padding: 0.65rem 1.25rem;
      border-radius: var(--radius-md);
      text-decoration: none;
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(245, 158, 11, 0.3);
    }

    .btn-download:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(245, 158, 11, 0.4);
    }

    main {
      max-width: 1300px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }

    /* Filters Section */
    .controls {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin-bottom: 2rem;
    }

    .search-bar {
      position: relative;
      width: 100%;
    }

    .search-bar input {
      width: 100%;
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 0.9rem 1.25rem 0.9rem 3rem;
      color: var(--text-main);
      font-size: 1rem;
      outline: none;
      transition: border-color 0.2s;
    }

    .search-bar input:focus {
      border-color: var(--primary);
    }

    .search-icon {
      position: absolute;
      left: 1rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
    }

    .filter-tabs {
      display: flex;
      gap: 0.5rem;
      overflow-x: auto;
      padding-bottom: 0.5rem;
      scrollbar-width: thin;
    }

    .tab-btn {
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 0.6rem 1.25rem;
      border-radius: var(--radius-md);
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }

    .tab-btn:hover {
      color: var(--text-main);
      background: rgba(51, 65, 85, 0.6);
    }

    .tab-btn.active {
      background: var(--primary);
      color: #0f172a;
      border-color: var(--primary);
    }

    .sub-filters {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .select-filter {
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.6rem 1rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      outline: none;
      cursor: pointer;
    }

    .stats-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
      color: var(--text-muted);
      font-size: 0.9rem;
    }

    /* Schedule Grid */
    .events-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 1.25rem;
    }

    .event-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
      position: relative;
      overflow: hidden;
    }

    .event-card:hover {
      transform: translateY(-4px);
      background: var(--bg-card-hover);
      border-color: rgba(245, 158, 11, 0.4);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }

    .event-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--primary);
    }

    /* Category colors */
    .event-card[data-cat*="Dança"]::before { background: #f59e0b; }
    .event-card[data-cat*="Concertos"]::before { background: #ec4899; }
    .event-card[data-cat*="Bailes"]::before { background: #8b5cf6; }
    .event-card[data-cat*="ELI"]::before { background: #10b981; }
    .event-card[data-cat*="Desenvolvimento"]::before { background: #06b6d4; }
    .event-card[data-cat*="Instrumentos"]::before { background: #f97316; }
    .event-card[data-cat*="Conversas"]::before { background: #3b82f6; }
    .event-card[data-cat*="Igreja"]::before { background: #eab308; }
    .event-card[data-cat*="Tradição"]::before { background: #84cc16; }
    .event-card[data-cat*="Viagens"]::before { background: #14b8a6; }

    .event-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.75rem;

    }

    .event-time {
      font-family: 'Outfit', sans-serif;
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-light);
      background: rgba(245, 158, 11, 0.1);
      padding: 0.2rem 0.6rem;
      border-radius: var(--radius-sm);
    }

    .event-date-badge {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
    }

    .event-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 0.4rem;
      line-height: 1.3;
    }

    .event-desc {
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
      line-height: 1.4;
    }

    .event-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 0.75rem;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      font-size: 0.8rem;
    }

    .event-location {
      font-weight: 600;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      gap: 0.3rem;
    }

    .event-cat {
      background: rgba(255, 255, 255, 0.08);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      color: var(--text-muted);
    }

    .no-results {
      grid-column: 1 / -1;
      text-align: center;
      padding: 4rem 2rem;
      background: var(--bg-card);
      border-radius: var(--radius-md);
      color: var(--text-muted);
    }

    @media (max-width: 768px) {
      header {
        padding: 1rem;
      }
      .brand h1 {
        font-size: 1.4rem;
      }
      .events-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>

  <header>
    <div class="header-container">
      <div class="brand">
        <h1>TRADIDANÇAS 2026</h1>
        <span class="dates">29 Jul - 2 Ago</span>
      </div>
      <div class="header-actions">
        <a href="tradidancas2026.ics" class="btn-download" download>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Baixar .ICS
        </a>
      </div>
    </div>
  </header>

  <main>
    <div class="controls">
      <div class="search-bar">
        <svg class="search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="searchInput" placeholder="Pesquisar por artista, dança, oficina ou local...">
      </div>

      <div class="filter-tabs" id="dayTabs">
        <button class="tab-btn active" data-day="all">Todos os Dias</button>
        <button class="tab-btn" data-day="2026-07-29">29 Jul (Qua)</button>
        <button class="tab-btn" data-day="2026-07-30">30 Jul (Qui)</button>
        <button class="tab-btn" data-day="2026-07-31">31 Jul (Sex)</button>
        <button class="tab-btn" data-day="2026-08-01">1 Ago (Sáb)</button>
        <button class="tab-btn" data-day="2026-08-02">2 Ago (Dom)</button>
      </div>

      <div class="sub-filters">
        <select id="stageFilter" class="select-filter">
          <option value="all">Todos os Palcos / Locais</option>
        </select>

        <select id="catFilter" class="select-filter">
          <option value="all">Todas as Categorias</option>
        </select>
      </div>
    </div>

    <div class="stats-bar">
      <span id="eventsCount">A carregar programa...</span>
      <span>São Pedro do Sul</span>
    </div>

    <div class="events-grid" id="eventsGrid">
      <!-- Events injected dynamically -->
    </div>
  </main>

  <script>
    const eventsData = JSON_EVENTS_DATA;

    const dayFormat = {
      '2026-07-29': 'Qua, 29 Jul',
      '2026-07-30': 'Qui, 30 Jul',
      '2026-07-31': 'Sex, 31 Jul',
      '2026-08-01': 'Sáb, 1 Ago',
      '2026-08-02': 'Dom, 2 Ago',
      '2026-08-03': 'Seg, 3 Ago (Madrugada)'
    };

    let currentDay = 'all';
    let currentStage = 'all';
    let currentCat = 'all';
    let searchQuery = '';

    // Populate dropdown filters
    function initFilters() {
      const stages = new Set();
      const categories = new Set();

      eventsData.forEach(ev => {
        if(ev.loc) stages.add(ev.loc);
        if(ev.cat) categories.add(ev.cat);
      });

      const stageSelect = document.getElementById('stageFilter');
      Array.from(stages).sort().forEach(st => {
        const opt = document.createElement('option');
        opt.value = st;
        opt.textContent = st;
        stageSelect.appendChild(opt);
      });

      const catSelect = document.getElementById('catFilter');
      Array.from(categories).sort().forEach(c => {
        const opt = document.createElement('option');
        opt.value = c;
        opt.textContent = c;
        catSelect.appendChild(opt);
      });
    }

    function renderEvents() {
      const grid = document.getElementById('eventsGrid');
      grid.innerHTML = '';

      const filtered = eventsData.filter(ev => {
        const matchDay = currentDay === 'all' || ev.date === currentDay;
        const matchStage = currentStage === 'all' || ev.loc === currentStage;
        const matchCat = currentCat === 'all' || ev.cat === currentCat;
        const matchSearch = searchQuery === '' || 
          ev.title.toLowerCase().includes(searchQuery) ||
          ev.desc.toLowerCase().includes(searchQuery) ||
          ev.loc.toLowerCase().includes(searchQuery);

        return matchDay && matchStage && matchCat && matchSearch;
      });

      document.getElementById('eventsCount').textContent = `${filtered.length} eventos encontrados`;

      if(filtered.length === 0) {
        grid.innerHTML = `<div class="no-results">Nenhum evento encontrado com os filtros selecionados.</div>`;
        return;
      }

      filtered.forEach(ev => {
        const card = document.createElement('div');
        card.className = 'event-card';
        card.setAttribute('data-cat', ev.cat || '');

        const formattedDate = dayFormat[ev.date] || ev.date;

        card.innerHTML = `
          <div>
            <div class="event-header">
              <span class="event-time">${ev.start} - ${ev.end}</span>
              <span class="event-date-badge">${formattedDate}</span>
            </div>
            <div class="event-title">${ev.title}</div>
            <div class="event-desc">${ev.desc}</div>
          </div>
          <div class="event-footer">
            <span class="event-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              ${ev.loc}
            </span>
            <span class="event-cat">${ev.cat}</span>
          </div>
        `;
        grid.appendChild(card);
      });
    }

    // Event Listeners
    document.getElementById('dayTabs').addEventListener('click', (e) => {
      if(e.target.classList.contains('tab-btn')) {
        document.querySelectorAll('#dayTabs .tab-btn').forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');
        currentDay = e.target.getAttribute('data-day');
        renderEvents();
      }
    });

    document.getElementById('stageFilter').addEventListener('change', (e) => {
      currentStage = e.target.value;
      renderEvents();
    });

    document.getElementById('catFilter').addEventListener('change', (e) => {
      currentCat = e.target.value;
      renderEvents();
    });

    document.getElementById('searchInput').addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      renderEvents();
    });

    // Init
    initFilters();
    renderEvents();
  </script>
</body>
</html>
"""

html_content = html_template.replace("JSON_EVENTS_DATA", json.dumps(events, ensure_ascii=False))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated index.html successfully.")
