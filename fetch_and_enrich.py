import urllib.request
import re
import html
import json
from datetime import datetime

# URLs to scrape and their categories
url_mapping = {
    'https://tradidancas.pt/oficina-de-dancas-e-bailes/': ['Oficinas de Dança', 'Bailes e Animações'],
    'https://tradidancas.pt/concertos-palco-serra/': ['Concertos'],
    'https://tradidancas.pt/concertos-igreja/': ['Igreja'],
    'https://tradidancas.pt/eli-espaco-ludico-intergeracional/': ['ELI - Lúdico Intergeracional', 'ELI - Outras Atividades'],
    'https://tradidancas.pt/oficinas-de-desenvolvimento-pessoal/': ['Desenvolvimento Pessoal - Eira', 'Desenvolvimento Pessoal - Palcos'],
    'https://tradidancas.pt/oficinas-de-instrumento-musical/': ['Instrumentos Musicais - Eira'],
    'https://tradidancas.pt/conversas/': ['Conversas - Eira'],
    'https://tradidancas.pt/laboratorio-da-tradicao/': ['Tradição e Ecologia'],
    'https://tradidancas.pt/viagens-de-natureza/': ['Viagens de Natureza'],
    'https://tradidancas.pt/animacao-de-rua-salao/': ['Cantos da Eira', 'Adega da Eira', 'Viagens de Tradição', 'Cantina']
}

scraped_blocks = [] # List of tuples: (url, text)

for url in url_mapping.keys():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        raw_html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        
        clean_html = re.sub(r'<script.*?>.*?</script>', '', raw_html, flags=re.DOTALL)
        clean_html = re.sub(r'<style.*?>.*?</style>', '', clean_html, flags=re.DOTALL)
        
        blocks = re.findall(r'<(h[1-6]|p|div|li)[^>]*>(.*?)</\1>', clean_html, flags=re.DOTALL)
        for tag, content in blocks:
            txt = re.sub(r'<[^>]+>', ' ', content)
            txt = html.unescape(txt).strip()
            txt = re.sub(r'\s+', ' ', txt)
            if len(txt) > 25 and not txt.startswith('http') and not txt.startswith('var '):
                scraped_blocks.append((url, txt))
    except Exception as e:
        print(f"Error scraping {url}: {e}")

print(f"Total scraped description blocks: {len(scraped_blocks)}")

# Load original events
from generate_ics import events

enriched_count = 0

for ev in events:
    title = ev["title"].lower()
    desc = ev["desc"].lower()
    cat = ev.get("cat", "")
    
    # Try finding relevant scraped block
    matches = []
    for url, block in scraped_blocks:
        block_lower = block.lower()
        keywords = set(re.findall(r'\w{4,}', title + " " + desc))
        matches_kws = [kw for kw in keywords if kw not in {'palco', 'oficina', 'dança', 'danças', 'concerto', 'baile', 'com'} and kw in block_lower]
        
        if len(matches_kws) >= 2 or (len(keywords) == 1 and len(matches_kws) == 1):
            matches.append((url, block))
    
    # Default URL based on category if no specific match
    default_url = None
    for target_url, categories in url_mapping.items():
        if cat in categories:
            default_url = target_url
            break
    if not default_url:
        default_url = "https://tradidancas.pt/programacao/"

    if matches:
        best_url, best_match = max(matches, key=lambda x: len(x[1]))
        if best_match not in ev["desc"]:
            ev["desc"] = f"{ev['desc']} | {best_match} | Mais info: {best_url}"
            ev["url"] = best_url
            enriched_count += 1
    else:
        ev["desc"] = f"{ev['desc']} | Mais info: {default_url}"
        ev["url"] = default_url

print(f"Enriched {enriched_count} events with detailed website descriptions and source URLs!")

# Regenerate ICS
lines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//Tradidanças 2026//Festival Calendar//PT",
    "CALSCALE:GREGORIAN",
    "METHOD:PUBLISH",
    "X-WR-CALNAME:Tradidanças 2026",
    "X-WR-TIMEZONE:Europe/Lisbon"
]

dtstamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

for idx, ev in enumerate(events, start=1):
    date_str = ev["date"].replace("-", "")
    sh, sm = ev["start"].split(":")
    eh, em = ev["end"].split(":")
    
    dtstart = f"{date_str}T{sh}{sm}00"
    dtend = f"{date_str}T{eh}{em}00"
    
    uid = f"tradidancas2026-evt-{idx:03d}@tradidancas.pt"
    
    clean_desc = ev['desc'].replace("\n", " ").replace("\r", " ")
    clean_title = ev['title'].replace("\n", " ")
    event_url = ev.get('url', 'https://tradidancas.pt/programacao/')
    
    lines.append("BEGIN:VEVENT")
    lines.append(f"UID:{uid}")
    lines.append(f"DTSTAMP:{dtstamp}")
    lines.append(f"DTSTART;TZID=Europe/Lisbon:{dtstart}")
    lines.append(f"DTEND;TZID=Europe/Lisbon:{dtend}")
    lines.append(f"SUMMARY:{clean_title}")
    lines.append(f"DESCRIPTION:{clean_desc}")
    lines.append(f"URL:{event_url}")
    lines.append(f"LOCATION:{ev['loc']}, Tradidanças (São Pedro do Sul)")
    lines.append(f"CATEGORIES:{ev['cat']}")
    lines.append("END:VEVENT")

lines.append("END:VCALENDAR")

ics_content = "\r\n".join(lines) + "\r\n"

with open("tradidancas2026.ics", "w", encoding="utf-8") as f:
    f.write(ics_content)

with open("tradidancas.ics", "w", encoding="utf-8") as f:
    f.write(ics_content)

# Update index.html
from create_html_app import html_template
html_content = html_template.replace("JSON_EVENTS_DATA", json.dumps(events, ensure_ascii=False))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated tradidancas2026.ics, tradidancas.ics, and index.html with URLs successfully.")
