import json
from fetch_and_enrich import events

# 1. Save formatted events.json
with open("events.json", "w", encoding="utf-8") as f:
    json.dump(events, f, indent=2, ensure_ascii=False)

print("Saved formatted events.json successfully.")

# 2. Update index.html to fetch events.json dynamically
html_content = """<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TRADIDANÇAS 2026 - Programa Não Oficial</title>
  <meta name="description" content="Programa completo e interativo do festival Tradidanças 2026 (29 Julho a 2 Agosto). Oficinas, concertos, bailes, conversas e viagens.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #0b1120;
      --bg-card: rgba(30, 41, 59, 0.75);
      --bg-card-hover: rgba(51, 65, 85, 0.85);
      --primary: #f59e0b;
      --primary-light: #fbbf24;
      --accent: #ec4899;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --border-color: rgba(255, 255, 255, 0.12);
      --glass-bg: rgba(11, 17, 32, 0.85);
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
        radial-gradient(at 10% 10%, rgba(245, 158, 11, 0.12) 0px, transparent 50%),
        radial-gradient(at 90% 20%, rgba(236, 72, 153, 0.12) 0px, transparent 50%),
        radial-gradient(at 50% 90%, rgba(16, 185, 129, 0.12) 0px, transparent 50%);
      background-attachment: fixed;
      padding-bottom: 80px;
    }

    header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--glass-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-color);
      padding: 1rem 1.5rem;
    }

    .header-container {
      max-width: 900px;
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
      font-size: 1.6rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      background: linear-gradient(135deg, #f59e0b 0%, #ec4899 50%, #3b82f6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand .dates {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.05);
      padding: 0.2rem 0.6rem;
      border-radius: 20px;
      border: 1px solid var(--border-color);
    }

    .header-buttons {
      display: flex;
      gap: 0.6rem;
    }

    .btn-action {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      font-weight: 600;
      font-size: 0.85rem;
      padding: 0.55rem 1rem;
      border-radius: var(--radius-md);
      text-decoration: none;
      transition: all 0.2s ease;
    }

    .btn-action:hover {
      background: rgba(51, 65, 85, 0.9);
      border-color: var(--primary);
    }

    .btn-primary {
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #0f172a;
      border: none;
      font-weight: 700;
      box-shadow: 0 4px 14px rgba(245, 158, 11, 0.25);
    }

    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(245, 158, 11, 0.35);
    }

    /* Disclaimer Banner */
    .disclaimer-banner {
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.3);
      color: #fca5a5;
      padding: 0.75rem 1.25rem;
      border-radius: var(--radius-md);
      margin-bottom: 1.5rem;
      font-size: 0.85rem;
      line-height: 1.4;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .disclaimer-banner a {
      color: #fff;
      font-weight: 600;
      text-decoration: underline;
    }

    main {
      max-width: 900px;
      margin: 1.5rem auto;
      padding: 0 1.25rem;
    }

    /* Controls Section */
    .controls {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin-bottom: 1.5rem;
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
      padding: 0.85rem 1.25rem 0.85rem 2.8rem;
      color: var(--text-main);
      font-size: 0.95rem;
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
      padding-bottom: 0.4rem;
      scrollbar-width: thin;
    }

    .tab-btn {
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 0.55rem 1.1rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
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
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .select-filter {
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.55rem 0.9rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      outline: none;
      cursor: pointer;
      flex: 1;
      min-width: 160px;
    }

    .stats-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.25rem;
      color: var(--text-muted);
      font-size: 0.85rem;
    }

    /* FULL WIDTH EVENTS LIST */
    .events-grid {
      display: flex;
      flex-direction: column;
      gap: 0.9rem;
      width: 100%;
    }

    .event-card {
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      transition: all 0.25s ease;
      position: relative;
      overflow: hidden;
      cursor: pointer;
      user-select: none;
    }

    .event-card:hover {
      background: var(--bg-card-hover);
      border-color: rgba(245, 158, 11, 0.4);
    }

    /* PAST EVENTS STYLING */
    .event-card.is-past {
      opacity: 0.45;
      filter: grayscale(85%);
    }

    .event-card.is-past:hover {
      opacity: 0.75;
      filter: grayscale(40%);
    }

    /* CURRENT / ONGOING EVENT STYLING */
    .event-card.is-current {
      border: 2px solid var(--primary-light);
      background: rgba(45, 55, 72, 0.9);
      box-shadow: 0 0 24px rgba(251, 191, 36, 0.35);
    }

    .event-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 5px;
      height: 100%;
      background: var(--primary);
    }

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
      align-items: center;
      margin-bottom: 0.5rem;
    }

    .event-time {
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-light);
      background: rgba(245, 158, 11, 0.12);
      padding: 0.2rem 0.6rem;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }

    .current-indicator {
      font-size: 0.7rem;
      font-weight: 800;
      color: #0f172a;
      background: var(--primary-light);
      padding: 0.1rem 0.4rem;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .event-date-badge {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-muted);
    }

    .event-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: 0.3rem;
      line-height: 1.35;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .toggle-icon {
      font-size: 0.85rem;
      color: var(--text-muted);
      transition: transform 0.25s ease;
    }

    .event-card.expanded .toggle-icon {
      transform: rotate(180deg);
      color: var(--primary);
    }

    .event-desc {
      font-size: 0.92rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-top: 0.6rem;
      max-height: 0;
      opacity: 0;
      overflow: hidden;
      transition: max-height 0.35s ease, opacity 0.3s ease, margin 0.3s ease;
    }

    .event-card.expanded .event-desc {
      max-height: 1000px;
      opacity: 1;
      margin-top: 0.75rem;
      padding-top: 0.75rem;
      border-top: 1px dashed rgba(255, 255, 255, 0.1);
    }

    .event-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 0.75rem;
      font-size: 0.82rem;
    }

    .event-location {
      font-weight: 600;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }

    .event-cat {
      background: rgba(255, 255, 255, 0.08);
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
      color: var(--text-muted);
    }

    .share-link {
      margin-top: 0.75rem;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.8rem;
      color: var(--primary-light);
      text-decoration: none;
      font-weight: 600;
    }

    .share-link:hover {
      text-decoration: underline;
    }

    .no-results {
      text-align: center;
      padding: 4rem 2rem;
      background: var(--bg-card);
      border-radius: var(--radius-md);
      color: var(--text-muted);
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
      <div class="header-buttons">
        <a href="events.json" class="btn-action" target="_blank">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          events.json
        </a>
        <a href="tradidancas2026.ics" class="btn-action btn-primary" download>
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Baixar .ICS
        </a>
      </div>
    </div>
  </header>

  <main>
    <div class="disclaimer-banner">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
      <div>
        <strong>Aviso Importante:</strong> Este website <strong>não é oficial</strong>. É uma ferramenta independente criada a partir da programação pública. Para a página oficial, visite <a href="https://tradidancas.pt" target="_blank" rel="noopener">tradidancas.pt</a>.
      </div>
    </div>

    <div class="controls">
      <div class="search-bar">
        <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="searchInput" placeholder="Pesquisar por artista, dança, oficina ou palco...">
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
      <!-- Full width events list injected dynamically -->
    </div>
  </main>

  <script>
    let eventsData = [];

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
    let autoScrolled = false;

    const now = new Date();
    const refNow = (now.getFullYear() === 2026 && now.getMonth() === 6 && now.getDate() >= 29 && now.getDate() <= 31) || (now.getFullYear() === 2026 && now.getMonth() === 7 && now.getDate() <= 3)
      ? now 
      : new Date("2026-07-29T13:12:00");

    function parseEventDate(dateStr, timeStr) {
      const [year, month, day] = dateStr.split('-').map(Number);
      const [hours, mins] = timeStr.split(':').map(Number);
      return new Date(year, month - 1, day, hours, mins, 0);
    }

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

    function getQueryParam(param) {
      const urlParams = new URLSearchParams(window.location.search);
      return urlParams.get(param);
    }

    function renderEvents() {
      const grid = document.getElementById('eventsGrid');
      grid.innerHTML = '';

      const targetEventId = getQueryParam('event');

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

      document.getElementById('eventsCount').textContent = `${filtered.length} eventos no programa`;

      if(filtered.length === 0) {
        grid.innerHTML = `<div class="no-results">Nenhum evento encontrado com os filtros selecionados.</div>`;
        return;
      }

      let currentElementToScroll = null;
      let targetSharedElement = null;

      filtered.forEach((ev, idx) => {
        const evId = `evt-${idx + 1}`;
        const card = document.createElement('div');
        card.className = 'event-card';
        card.id = evId;
        card.setAttribute('data-cat', ev.cat || '');

        const startDate = parseEventDate(ev.date, ev.start);
        const endDate = parseEventDate(ev.date, ev.end);

        const isPast = endDate < refNow;
        const isCurrent = startDate <= refNow && refNow <= endDate;

        if (isPast) card.classList.add('is-past');
        if (isCurrent) {
          card.classList.add('is-current');
          if (!currentElementToScroll) currentElementToScroll = card;
        } else if (!isPast && !currentElementToScroll) {
          currentElementToScroll = card;
        }

        const isTargetShared = targetEventId && (targetEventId === evId || targetEventId === String(idx + 1));
        if (isTargetShared) {
          card.classList.add('expanded');
          targetSharedElement = card;
        }

        const formattedDate = dayFormat[ev.date] || ev.date;

        card.innerHTML = `
          <div class="event-header">
            <span class="event-time">
              ${ev.start} - ${ev.end}
              ${isCurrent ? '<span class="current-indicator">A decorrer</span>' : ''}
            </span>
            <span class="event-date-badge">${formattedDate}</span>
          </div>
          <div class="event-title">
            <span>${ev.title}</span>
            <span class="toggle-icon">▼</span>
          </div>
          <div class="event-footer">
            <span class="event-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              ${ev.loc}
            </span>
            <span class="event-cat">${ev.cat}</span>
          </div>
          <div class="event-desc">
            <p>${ev.desc}</p>
            ${ev.url ? `<a href="${ev.url}" target="_blank" class="share-link" onclick="event.stopPropagation()">Ver na página oficial ↗</a>` : ''}
          </div>
        `;

        card.addEventListener('click', () => {
          const isExpanded = card.classList.contains('expanded');
          document.querySelectorAll('.event-card.expanded').forEach(c => {
            if(c !== card) c.classList.remove('expanded');
          });
          
          if (!isExpanded) {
            card.classList.add('expanded');
            const newUrl = new URL(window.location);
            newUrl.searchParams.set('event', evId);
            history.pushState(null, '', newUrl);
          } else {
            card.classList.remove('expanded');
            const newUrl = new URL(window.location);
            newUrl.searchParams.delete('event');
            history.pushState(null, '', newUrl);
          }
        });

        grid.appendChild(card);
      });

      if (!autoScrolled) {
        autoScrolled = true;
        const elemToScroll = targetSharedElement || currentElementToScroll;
        if (elemToScroll) {
          setTimeout(() => {
            const rect = elemToScroll.getBoundingClientRect();
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            const targetY = rect.top + scrollTop - (window.innerHeight * 0.25);
            window.scrollTo({ top: targetY, behavior: 'smooth' });
          }, 300);
        }
      }
    }

    // Load events.json
    fetch('events.json')
      .then(res => res.json())
      .then(data => {
        eventsData = data;
        initFilters();
        renderEvents();
      })
      .catch(err => {
        console.error('Error loading events.json:', err);
        document.getElementById('eventsGrid').innerHTML = `<div class="no-results">Erro ao carregar o ficheiro events.json.</div>`;
      });

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
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated index.html to fetch events.json dynamically.")
