import uuid
from datetime import datetime

events = [
    # PAGE 1: OFICINAS DE DANÇA
    # DIA 29 QUARTA-FEIRA (July 29, 2026)
    {"date": "2026-07-29", "start": "11:45", "end": "13:00", "loc": "Palco Carvalhais", "title": "Eu Não Sei Cantar a Bailar!", "desc": "Projecto 'Eu Não Sei Cantar'", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "14:00", "end": "15:15", "loc": "Palco Carvalhais", "title": "Gregas", "desc": "Trio Kajmak e Danai Anastasopoulou", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "14:00", "end": "15:15", "loc": "Palco Abados", "title": "Poitou", "desc": "Lisou&Sons", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "14:00", "end": "15:15", "loc": "Palco Inatel", "title": "Europeias", "desc": "Duo Bella Ciao e Diana Azevedo", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "14:00", "end": "15:15", "loc": "Palco Arada", "title": "Irlandesas", "desc": "Gandarva", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "15:30", "end": "16:45", "loc": "Palco Carvalhais", "title": "Países Catalães", "desc": "Radicel-la", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "15:30", "end": "16:45", "loc": "Palco Abados", "title": "Portuguesas", "desc": "No Mazurka Band", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "15:30", "end": "16:45", "loc": "Palco Inatel", "title": "Francesas", "desc": "Duo La Billebaude e Amélie Vaudelin", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "15:30", "end": "16:45", "loc": "Palco Arada", "title": "Bullerengue", "desc": "Entra na Roda", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "17:00", "end": "18:15", "loc": "Palco Carvalhais", "title": "Ceilidh", "desc": "The Ciderhouse Rebellion", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "17:00", "end": "18:15", "loc": "Palco Abados", "title": "Fusion Bellydance", "desc": "Piny Orchidaceae", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "17:00", "end": "18:15", "loc": "Palco Inatel", "title": "Forró para Todos", "desc": "Alinne Araújo", "cat": "Oficinas de Dança"},
    {"date": "2026-07-29", "start": "17:00", "end": "18:15", "loc": "Palco Arada", "title": "Kizomba e Semba", "desc": "Bonifácio Aurio & Cláudia da Cruz", "cat": "Oficinas de Dança"},

    # DIA 30 QUINTA-FEIRA (July 30, 2026)
    {"date": "2026-07-30", "start": "14:00", "end": "15:15", "loc": "Palco Carvalhais", "title": "Ceilidh", "desc": "The Ciderhouse Rebellion", "cat": "Oficinas de Dança"},
    {"date": "2026-07-30", "start": "14:00", "end": "15:15", "loc": "Palco Abados", "title": "Galegas", "desc": "Xoteiras", "cat": "Oficinas de Dança"},
    {"date": "2026-07-30", "start": "14:00", "end": "15:15", "loc": "Palco Inatel", "title": "Lindy Hop", "desc": "Bota Swing", "cat": "Oficinas de Dança"},
    {"date": "2026-07-30", "start": "14:00", "end": "15:15", "loc": "Palco Arada", "title": "Países Catalães", "desc": "Radicel-la", "cat": "Oficinas de Dança"},
    {"date": "2026-07-30", "start": "15:30", "end": "16:45", "loc": "Palco Carvalhais", "title": "Queres Dançar Comigo?", "desc": "Natércia Lameiro & Rosa Lopes Dias", "cat": "Oficinas de Dança"},
    {"date": "2026-07-30", "start": "15:30", "end": "16:45", "loc": "Palco Abados", "title": "Havaiana", "desc": "Diana Rego", "cat": "Oficinas de Dança"},
    {"date": "2026-07-30", "start": "15:30", "end": "16:45", "loc": "Palco Inatel", "title": "Europeias", "desc": "Duo Bella Ciao e Diana Azevedo", "cat": "Oficinas de Dança"},
    {"date": "2026-07-30", "start": "15:30", "end": "16:45", "loc": "Palco Arada", "title": "Kizomba e Semba", "desc": "Bonifácio Aurio & Cláudia da Cruz", "cat": "Oficinas de Dança"},
    {"date": "2026-07-30", "start": "17:00", "end": "18:15", "loc": "Palco Carvalhais", "title": "Forró", "desc": "Espaço Baião", "cat": "Oficinas de Dança"},
    {"date": "2026-07-30", "start": "17:00", "end": "18:15", "loc": "Palco Abados", "title": "Portuguesas", "desc": "A Salto à Rua", "cat": "Oficinas de Dança"},
    {"date": "2026-07-30", "start": "17:00", "end": "18:15", "loc": "Palco Inatel", "title": "Argentinas", "desc": "Angeles Fiallo Montero", "cat": "Oficinas de Dança"},
    {"date": "2026-07-30", "start": "17:00", "end": "18:15", "loc": "Palco Arada", "title": "Ucranianas", "desc": "Litá Folk Band", "cat": "Oficinas de Dança"},

    # DIA 31 SEXTA-FEIRA (July 31, 2026)
    {"date": "2026-07-31", "start": "11:45", "end": "13:00", "loc": "Palco Carvalhais", "title": "Dançar o Fado", "desc": "Dançarém", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "14:00", "end": "15:15", "loc": "Palco Carvalhais", "title": "Portuguesas", "desc": "GEFAC", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "14:00", "end": "15:15", "loc": "Palco Abados", "title": "Portuguesas", "desc": "No Mazurka Band", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "14:00", "end": "15:15", "loc": "Palco Inatel", "title": "Country Line Dance", "desc": "Luís Guerra", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "14:00", "end": "15:15", "loc": "Palco Arada", "title": "Diáspora Romani", "desc": "Marta Portugal Dias", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "15:30", "end": "16:45", "loc": "Palco Carvalhais", "title": "Gregas", "desc": "Trio Kajmak e Danai Anastasopoulou", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "15:30", "end": "16:45", "loc": "Palco Abados", "title": "Salsa", "desc": "André Madeira", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "15:30", "end": "16:45", "loc": "Palco Inatel", "title": "House Dance", "desc": "Leo Soulflow", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "15:30", "end": "16:45", "loc": "Palco Arada", "title": "Mantra Prática Coreográfica em Loop de Raiz Latino-Americana", "desc": "Lacerda", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "17:00", "end": "18:15", "loc": "Palco Carvalhais", "title": "Portuguesas Região de Lafões", "desc": "Rancho Folclórico e Etnográfico da Tileira", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "17:00", "end": "18:15", "loc": "Palco Abados", "title": "Tango Argentino", "desc": "Graciana Romeo Lisboa em Tango", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "17:00", "end": "18:15", "loc": "Palco Inatel", "title": "Hip Hop New School", "desc": "Telmo Santos", "cat": "Oficinas de Dança"},
    {"date": "2026-07-31", "start": "17:00", "end": "18:15", "loc": "Palco Arada", "title": "Europeias", "desc": "Trio da Praia", "cat": "Oficinas de Dança"},

    # DIA 1 SÁBADO (August 1, 2026)
    {"date": "2026-08-01", "start": "11:45", "end": "13:00", "loc": "Palco Carvalhais", "title": "Capoeira", "desc": "Professor Raposo Grupo Muzenza de Capoeira", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "11:45", "end": "13:00", "loc": "Palco Abados", "title": "Poitou", "desc": "Lisou&Sons", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "11:45", "end": "13:00", "loc": "Palco Inatel", "title": "Argentinas", "desc": "Angeles Fiallo Montero", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "11:45", "end": "13:00", "loc": "Palco Arada", "title": "Garba", "desc": "Kritika Thakur", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "14:00", "end": "15:15", "loc": "Palco Carvalhais", "title": "Tango Argentino", "desc": "Graciana Romeo Lisboa em Tango", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "14:00", "end": "15:15", "loc": "Palco Abados", "title": "Afrobeats", "desc": "Telmo Santos", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "14:00", "end": "15:15", "loc": "Palco Inatel", "title": "Forró para Todos", "desc": "Alinne Araújo", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "14:00", "end": "15:15", "loc": "Palco Arada", "title": "Ucranianas", "desc": "Litá Folk Band", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "15:30", "end": "16:45", "loc": "Palco Carvalhais", "title": "Forró", "desc": "Espaço Baião", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "15:30", "end": "16:45", "loc": "Palco Abados", "title": "Portuguesas", "desc": "A Salto à Rua", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "15:30", "end": "16:45", "loc": "Palco Inatel", "title": "Dançar o Fado", "desc": "Dançarém", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "15:30", "end": "16:45", "loc": "Palco Arada", "title": "Bollywood", "desc": "Kritika Thakur", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "17:00", "end": "18:15", "loc": "Palco Carvalhais", "title": "Portuguesas Beira Alta", "desc": "Rancho Folclórico de Carvalhais", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "17:00", "end": "18:15", "loc": "Palco Abados", "title": "Galegas", "desc": "Xoteiras", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "17:00", "end": "18:15", "loc": "Palco Inatel", "title": "Bachata", "desc": "André Madeira", "cat": "Oficinas de Dança"},
    {"date": "2026-08-01", "start": "17:00", "end": "18:15", "loc": "Palco Arada", "title": "Mantra Prática Coreográfica em Loop de Raiz Latino-Americana", "desc": "Lacerda", "cat": "Oficinas de Dança"},

    # DIA 2 DOMINGO (August 2, 2026)
    {"date": "2026-08-02", "start": "11:45", "end": "13:00", "loc": "Palco Carvalhais", "title": "Milonga", "desc": "Graciana Romeo Lisboa em Tango", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "11:45", "end": "13:00", "loc": "Palco Abados", "title": "Oriental", "desc": "Marta Portugal Dias", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "11:45", "end": "13:00", "loc": "Palco Inatel", "title": "Persa", "desc": "Diana Rego", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "11:45", "end": "13:00", "loc": "Palco Arada", "title": "Zumba na Caneca Bailarico Tugâ", "desc": "Rosana Pereira", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "14:00", "end": "15:15", "loc": "Palco Carvalhais", "title": "Forró", "desc": "Espaço Baião", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "14:00", "end": "15:15", "loc": "Palco Abados", "title": "Hip Hop Old School", "desc": "Telmo Santos", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "14:00", "end": "15:15", "loc": "Palco Inatel", "title": "Bhangra", "desc": "Kritika Thakur", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "14:00", "end": "15:15", "loc": "Palco Arada", "title": "Mapalé e Champeta", "desc": "Entra na Roda", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "15:30", "end": "16:45", "loc": "Palco Carvalhais", "title": "Portuguesas", "desc": "GEFAC", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "15:30", "end": "16:45", "loc": "Palco Abados", "title": "Capoeira", "desc": "Professor Raposo Grupo Muzenza de Capoeira", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "15:30", "end": "16:45", "loc": "Palco Inatel", "title": "Lindy Hop", "desc": "Bota Swing", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "15:30", "end": "16:45", "loc": "Palco Arada", "title": "Europeias", "desc": "Trio da Praia", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "17:00", "end": "18:15", "loc": "Palco Carvalhais", "title": "Madeirenses", "desc": "Grupo Folclórico Cultural e Recreativo da Quinta Grande | Câmara de Lobos", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "17:00", "end": "18:15", "loc": "Palco Abados", "title": "Country Line Dance", "desc": "Luís Guerra", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "17:00", "end": "18:15", "loc": "Palco Inatel", "title": "Pasodoble", "desc": "André Madeira", "cat": "Oficinas de Dança"},
    {"date": "2026-08-02", "start": "17:00", "end": "18:15", "loc": "Palco Arada", "title": "Irlandesas", "desc": "Gandarva", "cat": "Oficinas de Dança"},

    # PAGE 1: CONCERTOS - PALCO SERRA
    {"date": "2026-07-29", "start": "22:30", "end": "23:45", "loc": "Palco Serra", "title": "Urze de Lume", "desc": "Concerto Palco Serra", "cat": "Concertos"},
    {"date": "2026-07-30", "start": "22:30", "end": "23:45", "loc": "Palco Serra", "title": "Miguel Quitério", "desc": "Concerto Palco Serra", "cat": "Concertos"},
    {"date": "2026-07-31", "start": "22:30", "end": "23:45", "loc": "Palco Serra", "title": "Momi Maiga", "desc": "Concerto Palco Serra", "cat": "Concertos"},
    {"date": "2026-08-01", "start": "22:30", "end": "23:45", "loc": "Palco Serra", "title": "Serigosa", "desc": "Concerto Palco Serra", "cat": "Concertos"},
    {"date": "2026-08-02", "start": "22:30", "end": "23:45", "loc": "Palco Serra", "title": "Uxu Kalhus", "desc": "Concerto Palco Serra", "cat": "Concertos"},

    # PAGE 2: BAILES E ANIMAÇÕES
    # July 29
    {"date": "2026-07-29", "start": "21:00", "end": "22:30", "loc": "Palco Carvalhais", "title": "Baile: Trio Kajmak e Danai Anastasopoulou", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-29", "start": "21:00", "end": "22:30", "loc": "Palco Abados", "title": "Baile: Bonifácio Aurio & Cláudia da Cruz", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-29", "start": "21:00", "end": "22:30", "loc": "Palco Inatel", "title": "Baile: Duo Bella Ciao e Diana Azevedo", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-29", "start": "21:00", "end": "22:30", "loc": "Palco Arada", "title": "Baile: Gandarva", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-29", "start": "22:45", "end": "00:15", "next_day_end": False, "loc": "Palco Carvalhais", "title": "Baile: The Ciderhouse Rebellion", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-29", "start": "22:45", "end": "00:15", "next_day_end": False, "loc": "Palco Inatel", "title": "Baile: Alinne Araújo", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-29", "start": "22:45", "end": "00:15", "next_day_end": False, "loc": "Palco Arada", "title": "Baile: Entra na Roda", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-30", "start": "00:30", "end": "02:00", "loc": "Palco Carvalhais", "title": "Baile: Diana Rego", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-30", "start": "00:30", "end": "02:00", "loc": "Palco Abados", "title": "Baile: No Mazurka Band", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-30", "start": "00:30", "end": "02:00", "loc": "Palco Inatel", "title": "Baile: Duo La Billebaude", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-30", "start": "00:30", "end": "02:00", "loc": "Palco Arada", "title": "Baile: Ohxalá", "desc": "Baile e Animação", "cat": "Bailes e Animações"},

    # July 30
    {"date": "2026-07-30", "start": "20:30", "end": "22:00", "loc": "Palco Abados", "title": "Baile: Horabaixa Radicel-la", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-30", "start": "21:00", "end": "22:30", "loc": "Palco Carvalhais", "title": "Baile: Forró Harmonize", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-30", "start": "21:00", "end": "22:30", "loc": "Palco Abados", "title": "Baile: A Salto à Rua", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-30", "start": "21:00", "end": "22:30", "loc": "Palco Inatel", "title": "Baile: Duo Bella Ciao e Diana Azevedo", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-30", "start": "21:00", "end": "22:30", "loc": "Palco Arada", "title": "Baile: Litá Folk Band", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-30", "start": "22:45", "end": "00:15", "loc": "Palco Carvalhais", "title": "Baile: Bailobaile", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-30", "start": "22:45", "end": "00:15", "loc": "Palco Inatel", "title": "Baile: Caravela Sessions", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-30", "start": "22:45", "end": "00:15", "loc": "Palco Arada", "title": "Baile: Caio no Forró", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-31", "start": "00:30", "end": "02:00", "loc": "Palco Carvalhais", "title": "Baile: The Ciderhouse Rebellion", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-31", "start": "00:30", "end": "02:00", "loc": "Palco Abados", "title": "Baile: Xoteiras", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-31", "start": "00:30", "end": "02:00", "loc": "Palco Inatel", "title": "Baile: Natércia Lameiro Trio", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-31", "start": "00:30", "end": "02:00", "loc": "Palco Arada", "title": "Baile: Bonifácio Aurio & Cláudia da Cruz", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-31", "start": "02:15", "end": "03:45", "loc": "Palco Arada", "title": "Baile: Balskandal DJ", "desc": "Baile e Animação", "cat": "Bailes e Animações"},

    # July 31
    {"date": "2026-07-31", "start": "21:00", "end": "22:30", "loc": "Palco Carvalhais", "title": "Baile: Rancho Folclórico e Etnográfico da Tileira", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-31", "start": "21:00", "end": "22:30", "loc": "Palco Abados", "title": "Baile: No Mazurka Band", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-31", "start": "21:00", "end": "22:30", "loc": "Palco Inatel", "title": "Baile: Tucanas", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-31", "start": "21:00", "end": "22:30", "loc": "Palco Arada", "title": "Baile: Caio no Forró", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-31", "start": "22:45", "end": "00:15", "loc": "Palco Carvalhais", "title": "Baile: GEFAC", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-31", "start": "22:45", "end": "00:15", "loc": "Palco Inatel", "title": "Baile: Telmo Santos e André Madeira", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-07-31", "start": "22:45", "end": "00:15", "loc": "Palco Arada", "title": "Baile: Baldio", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "00:30", "end": "02:00", "loc": "Palco Carvalhais", "title": "Baile: Trio Kajmak e Danai Anastasopoulou", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "00:30", "end": "02:00", "loc": "Palco Abados", "title": "Baile: Orchidaceae Clubbing", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "00:30", "end": "02:00", "loc": "Palco Inatel", "title": "Baile: Kritika Thakur", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "00:30", "end": "02:00", "loc": "Palco Arada", "title": "Baile: Trio da Praia", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "02:15", "end": "03:45", "loc": "Palco Arada", "title": "Baile: Bistek Toe", "desc": "Baile e Animação", "cat": "Bailes e Animações"},

    # August 1
    {"date": "2026-08-01", "start": "20:00", "end": "21:30", "loc": "Palco Abados", "title": "Baile: Aixopluc", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "21:00", "end": "22:30", "loc": "Palco Carvalhais", "title": "Baile: Rancho Folclórico de Carvalhais", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "21:00", "end": "22:30", "loc": "Palco Abados", "title": "Baile: Xoteiras", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "21:00", "end": "22:30", "loc": "Palco Inatel", "title": "Baile: Duo La Billebaude", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "21:00", "end": "22:30", "loc": "Palco Arada", "title": "Baile: Baldio", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "22:45", "end": "00:15", "loc": "Palco Carvalhais", "title": "Baile: Forró Harmonize e Bloco Qui Nem Jiló", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "22:45", "end": "00:15", "loc": "Palco Inatel", "title": "Baile: Telmo Santos e André Madeira", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-01", "start": "22:45", "end": "00:15", "loc": "Palco Arada", "title": "Baile: Kritika Thakur", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-02", "start": "00:30", "end": "02:00", "loc": "Palco Carvalhais", "title": "Baile: Bailobaile", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-02", "start": "00:30", "end": "02:00", "loc": "Palco Abados", "title": "Baile: A Salto à Rua", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-02", "start": "00:30", "end": "02:00", "loc": "Palco Inatel", "title": "Baile: Alinne Araújo", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-02", "start": "00:30", "end": "02:00", "loc": "Palco Arada", "title": "Baile: Litá Folk Band", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-02", "start": "02:15", "end": "03:45", "loc": "Palco Arada", "title": "Baile: DJ Gaiteirinho e DJ Mariska", "desc": "Baile e Animação", "cat": "Bailes e Animações"},

    # August 2
    {"date": "2026-08-02", "start": "21:00", "end": "22:30", "loc": "Palco Carvalhais", "title": "Baile: Grupo Folclórico Cultural e Recreativo da Quinta Grande | Câmara de Lobos", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-02", "start": "21:00", "end": "22:30", "loc": "Palco Abados", "title": "Baile: Aixopluc", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-02", "start": "21:00", "end": "22:30", "loc": "Palco Inatel", "title": "Baile: Bota Swing", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-02", "start": "21:00", "end": "22:30", "loc": "Palco Arada", "title": "Baile: Trio da Praia", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-02", "start": "22:45", "end": "00:15", "loc": "Palco Carvalhais", "title": "Baile: GEFAC", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-02", "start": "22:45", "end": "00:15", "loc": "Palco Inatel", "title": "Baile: Tucanas", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-02", "start": "22:45", "end": "00:15", "loc": "Palco Arada", "title": "Baile: Gandarva", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-03", "start": "00:30", "end": "02:00", "loc": "Palco Carvalhais", "title": "Baile: Baião Vintage - Baile de Forró em Vinil", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-03", "start": "00:30", "end": "02:00", "loc": "Palco Abados", "title": "Baile: Telmo Santos e André Madeira", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-03", "start": "00:30", "end": "02:00", "loc": "Palco Inatel", "title": "Baile: Kritika Thakur", "desc": "Baile e Animação", "cat": "Bailes e Animações"},
    {"date": "2026-08-03", "start": "00:30", "end": "02:00", "loc": "Palco Arada", "title": "Baile: Entra na Roda", "desc": "Baile e Animação", "cat": "Bailes e Animações"},

    # PAGE 2: ELI - ESPAÇO LÚDICO-INTERGERACIONAL
    # July 29
    {"date": "2026-07-29", "start": "10:00", "end": "10:50", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Yoga em Família", "desc": "Gotinha Mágica Raquel Paiva", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-29", "start": "11:00", "end": "11:50", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Jogos Matemáticos", "desc": "Circo Matemático", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-29", "start": "12:00", "end": "12:50", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Tronkar Ritmos para Crianças", "desc": "Winga", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-29", "start": "14:00", "end": "14:45", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Zaína e a Oliveira Conto Musical", "desc": "Joana Amorim e Duncan Fox", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-29", "start": "14:50", "end": "16:10", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Estampar a Liberdade", "desc": "Urban Roots", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-29", "start": "16:20", "end": "17:00", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Folhas em Movimento", "desc": "F(Olha)/Leave", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-29", "start": "17:10", "end": "17:50", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Capoeira", "desc": "Associação Dandá Paulo Monteiro", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-29", "start": "18:00", "end": "19:00", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Criação e Construção de Aves-Raras", "desc": "Daniela Fernandes 5ª Oficina", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-29", "start": "21:00", "end": "21:50", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Contar Histórias", "desc": "Marco Luna e Zé Pedro Ramos 5ª Oficina", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-29", "start": "22:00", "end": "23:00", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "F(Olha)/Leave", "desc": "Martina Griewark Ambrózio Comove", "cat": "ELI - Lúdico Intergeracional"},

    # July 30
    {"date": "2026-07-30", "start": "10:00", "end": "10:45", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Dança Natura", "desc": "Rosana Pereira", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-30", "start": "10:50", "end": "11:50", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Massagem para Crianças*", "desc": "Marisa João", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-30", "start": "12:00", "end": "12:50", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Musicolândia", "desc": "Mariana Cancela", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-30", "start": "14:00", "end": "14:35", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Zástráspás", "desc": "Música para Bebés e Crianças", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-30", "start": "14:40", "end": "16:10", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Oficina de Carvão e Imagens que Deslizam", "desc": "Narayana | Joana Rita", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-30", "start": "16:15", "end": "17:20", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Origami", "desc": "Circo Matemático", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-30", "start": "17:25", "end": "18:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Arte com Especiarias: Cores, Cheiros e Texturas da Natureza", "desc": "Sara Barbosa", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-30", "start": "19:00", "end": "20:00", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Bailinho da Limonada", "desc": "DJ Limonada", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-30", "start": "21:00", "end": "21:50", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Ecocontos", "desc": "Joana Tartaruga, Andrea Vertessen e Teresa Charata", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-30", "start": "22:00", "end": "23:00", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Filha do Mar Teatro Infantil", "desc": "Patrícia Herdeiro e Álvaro Zubiaurr", "cat": "ELI - Lúdico Intergeracional"},

    # July 31
    {"date": "2026-07-31", "start": "10:00", "end": "10:45", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Aventuras do Roberto", "desc": "Pradiante Atelier", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-31", "start": "10:50", "end": "12:10", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Estampar a Liberdade", "desc": "Urban Roots", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-31", "start": "12:15", "end": "13:00", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Danças Argentinas", "desc": "Angeles Fiallo Montero", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-31", "start": "14:00", "end": "14:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Trocador de Histórias Desbocadas", "desc": "Zé Pedro Ramos | 5ª Oficina", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-31", "start": "15:00", "end": "15:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Yoga em Família", "desc": "Gotinha Mágica Raquel Paiva", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-31", "start": "16:00", "end": "16:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Capoeira", "desc": "Associação Dandá Paulo Monteiro", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-31", "start": "17:00", "end": "17:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Carantonhas nas Árvores", "desc": "Plin Play in Nature | Adrimag", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-31", "start": "18:00", "end": "19:00", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Oficina de Brinquedos Tradicionais", "desc": "Ilídio Magueija | Adrimag", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-31", "start": "18:00", "end": "19:00", "loc": "Farmácia da Misericórdia", "title": "Farmácia e o Ambiente", "desc": "Isabel Serra (Farmácia da Misericórdia)", "cat": "ELI - Outras Atividades"},
    {"date": "2026-07-31", "start": "21:00", "end": "21:40", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Fado Bebé Canções e Tradições", "desc": "MBBC Música Bebés e Crianças", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-07-31", "start": "21:45", "end": "22:45", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Circo Matemático Show", "desc": "Circo Matemático", "cat": "ELI - Lúdico Intergeracional"},

    # August 1
    {"date": "2026-08-01", "start": "10:00", "end": "10:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Zaína e a Oliveira Conto Musical", "desc": "Joana Amorim e Duncan Fox", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-01", "start": "11:00", "end": "11:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "O Planeta Magicando", "desc": "Magicando", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-01", "start": "12:00", "end": "13:00", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Contos com Cantos", "desc": "Rosalinda das Cabras e as Jamigas das Modas", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-01", "start": "14:00", "end": "14:40", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "O Voo das Palavras", "desc": "Maria João Miguel", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-01", "start": "14:45", "end": "15:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Jogos Matemáticos", "desc": "Circo Matemático", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-01", "start": "16:00", "end": "16:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Dança Natura", "desc": "Rosana Pereira", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-01", "start": "17:00", "end": "17:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Tronkar Ritmos para Crianças", "desc": "Winga", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-01", "start": "18:00", "end": "19:00", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Bailinho Encantado do Jilo", "desc": "Espaço Baião", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-01", "start": "18:00", "end": "19:00", "loc": "Farmácia da Misericórdia", "title": "Cuidado com o Sol", "desc": "Farmácia da Misericórdia", "cat": "ELI - Outras Atividades"},
    {"date": "2026-08-01", "start": "21:00", "end": "21:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "O Voo das Palavras", "desc": "Maria João Miguel", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-01", "start": "22:00", "end": "23:00", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Momento Absurdo", "desc": "Tânia Safaneta Clown", "cat": "ELI - Lúdico Intergeracional"},

    # August 2
    {"date": "2026-08-02", "start": "10:00", "end": "10:35", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Zástráspás", "desc": "Música para Bebés e Crianças", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-02", "start": "10:40", "end": "11:25", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Danças Argentinas", "desc": "Angeles Fiallo Montero", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-02", "start": "11:30", "end": "12:30", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Música com as Próprias Mãos: Construção de Instrumentos e Dinamização Musical", "desc": "Goreti Mourão", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-02", "start": "14:00", "end": "14:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Filha do Mar Teatro Infantil", "desc": "Patrícia Herdeiro e Álvaro Zubiaurr", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-02", "start": "15:00", "end": "16:40", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Criação, Construção e Desfile de Aves-Raras", "desc": "Daniela Fernandes 5ª Oficina", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-02", "start": "16:45", "end": "17:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Origami", "desc": "Circo Matemático", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-02", "start": "18:00", "end": "19:10", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Oficina de Carvão e Imagens que Deslizam", "desc": "Narayana | Joana Rita", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-02", "start": "19:15", "end": "20:15", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Massagem para Crianças*", "desc": "Marisa João", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-02", "start": "21:00", "end": "21:55", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Trocador de Histórias Desbocadas", "desc": "Zé Pedro Ramos | 5ª Oficina", "cat": "ELI - Lúdico Intergeracional"},
    {"date": "2026-08-02", "start": "22:00", "end": "23:00", "loc": "Espaço Lúdico-Intergeracional (ELI)", "title": "Fado Bebé Canções e Tradições", "desc": "MBBC Música Bebés e Crianças", "cat": "ELI - Lúdico Intergeracional"},

    # PAGE 3: OFICINAS DE DESENVOLVIMENTO PESSOAL - EIRA
    {"date": "2026-07-29", "start": "09:30", "end": "10:45", "loc": "Eira", "title": "Chi Kung", "desc": "Inês Caeiro", "cat": "Desenvolvimento Pessoal - Eira"},
    {"date": "2026-07-30", "start": "09:30", "end": "10:45", "loc": "Eira", "title": "Power Yoga", "desc": "Márcio Silva", "cat": "Desenvolvimento Pessoal - Eira"},
    {"date": "2026-07-31", "start": "09:30", "end": "10:45", "loc": "Eira", "title": "Chi Kung: Corpo como Raiz e Asas", "desc": "Marta Horta | Escuta-te", "cat": "Desenvolvimento Pessoal - Eira"},
    {"date": "2026-08-01", "start": "09:30", "end": "10:45", "loc": "Eira", "title": "Conexão com a Natureza", "desc": "Sutura", "cat": "Desenvolvimento Pessoal - Eira"},
    {"date": "2026-08-02", "start": "09:30", "end": "10:45", "loc": "Eira", "title": "Yin Yang Tai Chi a Par", "desc": "Telmo Oliveira", "cat": "Desenvolvimento Pessoal - Eira"},

    # PAGE 3: OFICINAS DE INSTRUMENTOS MUSICAIS - EIRA
    {"date": "2026-07-29", "start": "11:15", "end": "12:30", "loc": "Eira", "title": "Jamicionário", "desc": "João Valente", "cat": "Instrumentos Musicais - Eira"},
    {"date": "2026-07-30", "start": "14:30", "end": "15:45", "loc": "Eira", "title": "Ensemble Folk", "desc": "Denys Stetsenko", "cat": "Instrumentos Musicais - Eira"},
    {"date": "2026-07-30", "start": "16:00", "end": "17:15", "loc": "Eira", "title": "Didgeridoo", "desc": "Renato Oliveira", "cat": "Instrumentos Musicais - Eira"},
    {"date": "2026-07-31", "start": "11:15", "end": "12:30", "loc": "Eira", "title": "Chora Baião", "desc": "Caio no Forró", "cat": "Instrumentos Musicais - Eira"},
    {"date": "2026-07-31", "start": "14:30", "end": "15:45", "loc": "Eira", "title": "Roncos, Voz e Bombo", "desc": "Mário Estanislau e Tiago Sami Pereira", "cat": "Instrumentos Musicais - Eira"},
    {"date": "2026-08-01", "start": "14:30", "end": "15:45", "loc": "Eira", "title": "Acalanto | Canções de Embalar do Mundo", "desc": "Maria Qué", "cat": "Instrumentos Musicais - Eira"},
    {"date": "2026-08-01", "start": "16:00", "end": "17:15", "loc": "Eira", "title": "A Voz das Mãos - Aprender Língua Gestual", "desc": "Paula Teixeira", "cat": "Instrumentos Musicais - Eira"},
    {"date": "2026-08-01", "start": "17:15", "end": "18:30", "loc": "Eira", "title": "Viola Campaniça Concerto Comentado", "desc": "Raia | Tozé Bexiga", "cat": "Instrumentos Musicais - Eira"},
    {"date": "2026-08-02", "start": "11:15", "end": "12:30", "loc": "Eira", "title": "Jam Session", "desc": "Laurent Geoffroy & Baltazar Montanaro", "cat": "Instrumentos Musicais - Eira"},
    {"date": "2026-08-02", "start": "14:30", "end": "15:45", "loc": "Eira", "title": "Percussão Ucraniana", "desc": "Litá Folk Band", "cat": "Instrumentos Musicais - Eira"},

    # PAGE 3: CONVERSAS - EIRA
    {"date": "2026-07-29", "start": "14:30", "end": "15:30", "loc": "Eira", "title": "Como Planear uma Cicloviagem", "desc": "Pedalanças", "cat": "Conversas - Eira"},
    {"date": "2026-07-29", "start": "15:45", "end": "17:00", "loc": "Eira", "title": "Dez Anos Fora do Guião: Uma Conversa sobre Liberdade e Raízes", "desc": "Meio Cheio", "cat": "Conversas - Eira"},
    {"date": "2026-07-29", "start": "17:20", "end": "18:30", "loc": "Eira", "title": "Dance Against the Machine", "desc": "Margarida Almeida | FEMFMUP", "cat": "Conversas - Eira"},
    {"date": "2026-07-30", "start": "11:15", "end": "12:30", "loc": "Eira", "title": "Os Zés Pereiras: Uma Cultura Musical do Entre Douro e Minho", "desc": "Napoleão Ribeiro", "cat": "Conversas - Eira"},
    {"date": "2026-07-30", "start": "17:30", "end": "18:30", "loc": "Eira", "title": "Interpretação de Sonhos", "desc": "Marta Seixas", "cat": "Conversas - Eira"},
    {"date": "2026-07-31", "start": "15:00", "end": "16:15", "loc": "Eira", "title": "Projeto Retrançar", "desc": "Técnic@s Sociais das Entidades Participantes", "cat": "Conversas - Eira"},
    {"date": "2026-07-31", "start": "17:30", "end": "18:30", "loc": "Eira", "title": "Queres Dançar Comigo?", "desc": "Natércia Lameiro & Rosa Lopes Dias", "cat": "Conversas - Eira"},
    {"date": "2026-08-01", "start": "11:15", "end": "12:30", "loc": "Eira", "title": "Dos Bailes aos Palcos: A Construção da História do Forró sob a Perspetiva das Mulheres", "desc": "Alinne Araújo, Eva Barros, Gisa Sabino e Xyss Bastos", "cat": "Conversas - Eira"},
    {"date": "2026-08-02", "start": "15:45", "end": "17:00", "loc": "Eira", "title": "Pausa Criativa: Fanzine", "desc": "Ser em Processo e Viagens em Mim", "cat": "Conversas - Eira"},
    {"date": "2026-08-02", "start": "17:20", "end": "18:30", "loc": "Eira", "title": "Boas Escolhas de Vida para uma Longevidade Saudável", "desc": "João Malva (CHANGEING), Anabela Marisa Azul (PAS-GRAS), Ana Duarte (HEALTH RISE), Fábio Reis (RDEFINE) e Paulo Oliveira (PAS-GRAS)", "cat": "Conversas - Eira"},

    # PAGE 3: CANTOS DA EIRA
    {"date": "2026-07-29", "start": "18:30", "end": "19:30", "loc": "Eira", "title": "Canto Tradicional Eslavo | Canções sobre as Plantas", "desc": "Greta Wardega", "cat": "Cantos da Eira"},
    {"date": "2026-07-30", "start": "18:30", "end": "19:30", "loc": "Eira", "title": "Oficina de Canto e Percussão", "desc": "Roda de Percussão Ibérica", "cat": "Cantos da Eira"},
    {"date": "2026-07-31", "start": "18:30", "end": "19:30", "loc": "Eira", "title": "Canto Tradicional Ibérico", "desc": "Serigosa", "cat": "Cantos da Eira"},
    {"date": "2026-08-01", "start": "18:30", "end": "19:30", "loc": "Eira", "title": "Canto Tradicional Ucraniano", "desc": "Litá Folk Band", "cat": "Cantos da Eira"},
    {"date": "2026-08-02", "start": "18:30", "end": "19:30", "loc": "Eira", "title": "Canto no Corpo", "desc": "Joana Alegre", "cat": "Cantos da Eira"},

    # PAGE 3: ADEGA DA EIRA
    {"date": "2026-07-29", "start": "20:00", "end": "21:00", "loc": "Adega da Eira", "title": "Micro-contos para Poucos de Cada Vez", "desc": "Luís Fernandes | D'Orfeu AC", "cat": "Adega da Eira"},
    {"date": "2026-07-30", "start": "20:00", "end": "21:00", "loc": "Adega da Eira", "title": "Micro-contos para Poucos de Cada Vez", "desc": "Luís Fernandes | D'Orfeu AC", "cat": "Adega da Eira"},
    {"date": "2026-07-31", "start": "20:00", "end": "21:00", "loc": "Adega da Eira", "title": "Micro-contos para Poucos de Cada Vez", "desc": "Luís Fernandes | D'Orfeu AC", "cat": "Adega da Eira"},
    {"date": "2026-08-01", "start": "20:00", "end": "21:00", "loc": "Adega da Eira", "title": "Micro-contos para Poucos de Cada Vez", "desc": "Luís Fernandes | D'Orfeu AC", "cat": "Adega da Eira"},

    # PAGE 3: LABORATÓRIO DA TRADIÇÃO E DA ECOLOGIA
    {"date": "2026-07-29", "start": "11:00", "end": "12:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Pausa Criativa: Postal e Abertura do Mural", "desc": "Ser em Processo e Viagens em Mim", "cat": "Tradição e Ecologia"},
    {"date": "2026-07-29", "start": "14:00", "end": "15:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Dorodengo - Bola de Barro Pólida", "desc": "Escola Regenerativa de Forniçô", "cat": "Tradição e Ecologia"},
    {"date": "2026-07-29", "start": "16:00", "end": "17:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Velas que Cuidam", "desc": "Inês Carreiró | Adrimag", "cat": "Tradição e Ecologia"},
    {"date": "2026-07-29", "start": "18:00", "end": "19:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Esguedelhada de Manhouce", "desc": "Sandra Costa e Mulheres de Manhouce | Adrimag", "cat": "Tradição e Ecologia"},

    {"date": "2026-07-30", "start": "09:30", "end": "11:00", "loc": "Laboratório da Tradição e da Ecologia", "title": "Alquimia da Cor Natural", "desc": "Ombu Atelier", "cat": "Tradição e Ecologia"},
    {"date": "2026-07-30", "start": "11:00", "end": "12:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Bruma Hidratante de Lavanda", "desc": "Fitore", "cat": "Tradição e Ecologia"},
    {"date": "2026-07-30", "start": "14:00", "end": "15:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Radical Electric", "desc": "Soliant Energy Farol do Colibri", "cat": "Tradição e Ecologia"},
    {"date": "2026-07-30", "start": "16:00", "end": "17:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Detergentes Caseiros Pastilhas Máquina Louça e Detergente Máquina Roupa", "desc": "Casadepau", "cat": "Tradição e Ecologia"},
    {"date": "2026-07-30", "start": "18:00", "end": "19:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Bolacha de Raiz", "desc": "Catarina Pinheiro | Adrimag", "cat": "Tradição e Ecologia"},

    {"date": "2026-07-31", "start": "09:30", "end": "11:00", "loc": "Laboratório da Tradição e da Ecologia", "title": "Descobrir o Cânhamo: Da Planta ao Fio", "desc": "7 Irmãs", "cat": "Tradição e Ecologia"},
    {"date": "2026-07-31", "start": "11:00", "end": "12:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Bombas de Sementes", "desc": "Rebel Orchidaceae", "cat": "Tradição e Ecologia"},
    {"date": "2026-07-31", "start": "14:00", "end": "15:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Oficina de Compostagem com Minhocas (Vermicompostagem)", "desc": "Revolução das Minhocas Emanuel Figueiredo e Pierre Del Cos", "cat": "Tradição e Ecologia"},
    {"date": "2026-07-31", "start": "16:00", "end": "17:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Pão de Ló de Oliveira de Sul", "desc": "Lurdes Bragança | Adrimag", "cat": "Tradição e Ecologia"},
    {"date": "2026-07-31", "start": "18:00", "end": "19:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Doces e Compotas Artesanais", "desc": "Mininês | Adrimag", "cat": "Tradição e Ecologia"},

    {"date": "2026-08-01", "start": "09:30", "end": "11:00", "loc": "Laboratório da Tradição e da Ecologia", "title": "Coroa Silvestre", "desc": "Olga Belyakova", "cat": "Tradição e Ecologia"},
    {"date": "2026-08-01", "start": "11:00", "end": "12:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Impressão Botânica com as Plantas do Tradidanças", "desc": "Tinctorium Studio", "cat": "Tradição e Ecologia"},
    {"date": "2026-08-01", "start": "14:00", "end": "15:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Saneamento Ecológico no Tradidanças", "desc": "Microvida", "cat": "Tradição e Ecologia"},
    {"date": "2026-08-01", "start": "16:00", "end": "17:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Broa de Milho do Candal", "desc": "Ana Martins e Custódia Oliveira | Adrimag", "cat": "Tradição e Ecologia"},
    {"date": "2026-08-01", "start": "18:00", "end": "19:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Trajes Tradicionais de Portugal", "desc": "Maria Duarte | Adrimag", "cat": "Tradição e Ecologia"},

    {"date": "2026-08-02", "start": "09:30", "end": "11:00", "loc": "Laboratório da Tradição e da Ecologia", "title": "Receitas Naturais para Auto-Cuidado", "desc": "Sofia da Cunha Seno", "cat": "Tradição e Ecologia"},
    {"date": "2026-08-02", "start": "11:00", "end": "12:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Mecânica de Bicicletas para Iniciantes", "desc": "Pedalanças", "cat": "Tradição e Ecologia"},
    {"date": "2026-08-02", "start": "14:00", "end": "15:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Planeamento e Gestão de uma Agro-Floresta", "desc": "Paulo Andrade", "cat": "Tradição e Ecologia"},
    {"date": "2026-08-02", "start": "16:00", "end": "17:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Arte de Trabalhar e Moldar a Cera", "desc": "Vítor Tavares", "cat": "Tradição e Ecologia"},
    {"date": "2026-08-02", "start": "18:00", "end": "19:30", "loc": "Laboratório da Tradição e da Ecologia", "title": "Mel da Serra da Arada", "desc": "José Gomes", "cat": "Tradição e Ecologia"},

    # PAGE 4: IGREJA
    {"date": "2026-07-29", "start": "17:00", "end": "18:00", "loc": "Igreja", "title": "Edgar Valente apresenta Ignorante", "desc": "Concerto Igreja", "cat": "Igreja"},
    {"date": "2026-07-29", "start": "18:00", "end": "19:00", "loc": "Igreja", "title": "Adélia (Concerto)", "desc": "Concerto Igreja", "cat": "Igreja"},
    {"date": "2026-07-29", "start": "19:00", "end": "20:00", "loc": "Igreja", "title": "Lucis Chorus (Concerto)", "desc": "Concerto Igreja", "cat": "Igreja"},

    {"date": "2026-07-30", "start": "17:00", "end": "18:00", "loc": "Igreja", "title": "Duo Soprano Arquialúde - Ana Leonor Pereira e Diana Matos", "desc": "Amores e Lamentos Música do Renascimento", "cat": "Igreja"},
    {"date": "2026-07-30", "start": "18:00", "end": "19:00", "loc": "Igreja", "title": "Sutura (Concerto de Conexão com a Natureza)", "desc": "Concerto Igreja", "cat": "Igreja"},
    {"date": "2026-07-30", "start": "19:00", "end": "20:00", "loc": "Igreja", "title": "The Ciderhouse Rebellion (Concerto)", "desc": "Concerto Igreja", "cat": "Igreja"},

    {"date": "2026-07-31", "start": "15:00", "end": "16:30", "loc": "Igreja", "title": "Fronteira do Medo Fumaça", "desc": "Escuta Coletiva", "cat": "Igreja"},
    {"date": "2026-07-31", "start": "17:00", "end": "18:00", "loc": "Igreja", "title": "Litá Folk Band (Concerto)", "desc": "Concerto Igreja", "cat": "Igreja"},
    {"date": "2026-07-31", "start": "18:00", "end": "19:00", "loc": "Igreja", "title": "Duo La Billebaude (Concerto)", "desc": "Concerto Igreja", "cat": "Igreja"},
    {"date": "2026-07-31", "start": "19:00", "end": "20:00", "loc": "Igreja", "title": "Roda de Percussão Ibérica (Concerto)", "desc": "Concerto Igreja", "cat": "Igreja"},

    {"date": "2026-08-01", "start": "15:00", "end": "16:30", "loc": "Igreja", "title": "Cramol, Vozes de Manhouce e Grupo de Cantares de Irijo e Souto-Chão", "desc": "Encontro de Canto a Vozes", "cat": "Igreja"},
    {"date": "2026-08-01", "start": "19:00", "end": "20:00", "loc": "Igreja", "title": "Joana Alegre (Concerto)", "desc": "Concerto Igreja", "cat": "Igreja"},
    {"date": "2026-08-01", "start": "20:00", "end": "21:00", "loc": "Igreja", "title": "Lauren (Concerto)", "desc": "Concerto Igreja", "cat": "Igreja"},

    {"date": "2026-08-02", "start": "16:00", "end": "17:00", "loc": "Igreja", "title": "Aixopluc (Concerto)", "desc": "Concerto Igreja", "cat": "Igreja"},
    {"date": "2026-08-02", "start": "17:00", "end": "18:00", "loc": "Igreja", "title": "Vozes da Terra", "desc": "Missa Dominical", "cat": "Igreja"},
    {"date": "2026-08-02", "start": "18:00", "end": "19:00", "loc": "Igreja", "title": "Caio e Eva (Concerto)", "desc": "Concerto Igreja", "cat": "Igreja"},
    {"date": "2026-08-02", "start": "19:00", "end": "20:00", "loc": "Igreja", "title": "Ana Laíns (Concerto)", "desc": "Concerto Igreja", "cat": "Igreja"},

    # PAGE 4: OFICINAS DE DESENVOLVIMENTO PESSOAL - PALCOS
    # July 29
    {"date": "2026-07-29", "start": "18:30", "end": "19:45", "loc": "Palco Carvalhais", "title": "Biodanza", "desc": "Inês Caeiro", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-07-29", "start": "18:30", "end": "19:45", "loc": "Palco Abados", "title": "Sentir", "desc": "Inês Pinto Cardoso", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-07-29", "start": "18:30", "end": "19:45", "loc": "Palco Inatel", "title": "Massagem Ayurvédica*", "desc": "Sofia Jorge", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-07-29", "start": "18:30", "end": "19:45", "loc": "Palco Arada", "title": "Power Yoga*", "desc": "Márcio Silva", "cat": "Desenvolvimento Pessoal - Palcos"},

    # July 30
    {"date": "2026-07-30", "start": "18:30", "end": "19:45", "loc": "Palco Carvalhais", "title": "Yoga e Vibrações Sagradas*", "desc": "Oriane", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-07-30", "start": "18:30", "end": "19:45", "loc": "Palco Abados", "title": "Yin Yang Tai Chi a Par", "desc": "Telmo Oliveira", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-07-30", "start": "18:30", "end": "19:45", "loc": "Palco Inatel", "title": "Wonder Sense: Império dos Sentidos*", "desc": "Ser Ama", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-07-30", "start": "18:30", "end": "19:45", "loc": "Palco Arada", "title": "Partner Yoga", "desc": "Catarina Silva e Guilherme Granato", "cat": "Desenvolvimento Pessoal - Palcos"},

    # July 31
    {"date": "2026-07-31", "start": "18:30", "end": "19:45", "loc": "Palco Carvalhais", "title": "Yoga e Movimento Somático*", "desc": "Cláudia Klages", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-07-31", "start": "18:30", "end": "19:45", "loc": "Palco Abados", "title": "Dança Criativa e Conexão Fascial", "desc": "Sofia da Mar e Barqueiro de Oz", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-07-31", "start": "18:30", "end": "19:45", "loc": "Palco Inatel", "title": "Sound Healing Journey*", "desc": "Sons Mágicos", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-07-31", "start": "18:30", "end": "19:45", "loc": "Palco Arada", "title": "Sentir", "desc": "Inês Pinto Cardoso", "cat": "Desenvolvimento Pessoal - Palcos"},

    # August 1
    {"date": "2026-08-01", "start": "10:00", "end": "11:15", "loc": "Palco Carvalhais", "title": "Pilates Clínico*", "desc": "Inês Oliveira", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-01", "start": "10:00", "end": "11:15", "loc": "Palco Abados", "title": "Sentir", "desc": "Inês Pinto Cardoso", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-01", "start": "10:00", "end": "11:15", "loc": "Palco Inatel", "title": "Massagem Ayurvédica*", "desc": "Sofia Jorge", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-01", "start": "10:00", "end": "11:15", "loc": "Palco Arada", "title": "Partner Yoga", "desc": "Catarina Silva e Guilherme Granato", "cat": "Desenvolvimento Pessoal - Palcos"},

    {"date": "2026-08-01", "start": "18:30", "end": "19:45", "loc": "Palco Carvalhais", "title": "Yoga e Vibrações Sagradas*", "desc": "Oriane", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-01", "start": "18:30", "end": "19:45", "loc": "Palco Abados", "title": "Biodanza", "desc": "Inês Caeiro", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-01", "start": "18:30", "end": "19:45", "loc": "Palco Inatel", "title": "Entre Bailes e Barrigas", "desc": "Amor ao Parto | Rita Araújo", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-01", "start": "18:30", "end": "19:45", "loc": "Palco Arada", "title": "7 Ritmos Sagrados do Mundo", "desc": "Diana Rego", "cat": "Desenvolvimento Pessoal - Palcos"},

    # August 2
    {"date": "2026-08-02", "start": "10:00", "end": "11:15", "loc": "Palco Carvalhais", "title": "Hypnobirthing para Todos", "desc": "Amor ao Parto | Rita Araújo", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-02", "start": "10:00", "end": "11:15", "loc": "Palco Abados", "title": "Yoga e Movimento Somático*", "desc": "Cláudia Klages", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-02", "start": "10:00", "end": "11:15", "loc": "Palco Inatel", "title": "Ecstatic Dance", "desc": "Sérgio Cristo", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-02", "start": "10:00", "end": "11:15", "loc": "Palco Arada", "title": "Wonder Sense: Império dos Sentidos*", "desc": "Ser Ama", "cat": "Desenvolvimento Pessoal - Palcos"},

    {"date": "2026-08-02", "start": "18:30", "end": "19:45", "loc": "Palco Carvalhais", "title": "Cerimónia Sufi", "desc": "Diana Rego", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-02", "start": "18:30", "end": "19:45", "loc": "Palco Abados", "title": "Dança Criativa e Conexão Fascial", "desc": "Sofia da Mar e Barqueiro de Oz", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-02", "start": "18:30", "end": "19:45", "loc": "Palco Inatel", "title": "Pilates Clínico*", "desc": "Inês Oliveira", "cat": "Desenvolvimento Pessoal - Palcos"},
    {"date": "2026-08-02", "start": "18:30", "end": "19:45", "loc": "Palco Arada", "title": "Chi Kung Corpo como Raiz e Asas", "desc": "Marta Horta | Escuta-te", "cat": "Desenvolvimento Pessoal - Palcos"},

    # PAGE 4: VIAGENS DE NATUREZA
    {"date": "2026-07-29", "start": "10:00", "end": "12:00", "loc": "Viagens de Natureza", "title": "Caminhada com Construção de Instrumentos Musicais Singelos", "desc": "Napoleão Ribeiro", "cat": "Viagens de Natureza"},
    {"date": "2026-07-30", "start": "09:30", "end": "11:30", "loc": "Viagens de Natureza", "title": "Pedalada ao Poço Azul", "desc": "Pedalanças", "cat": "Viagens de Natureza"},
    {"date": "2026-07-30", "start": "10:00", "end": "12:00", "loc": "Viagens de Natureza", "title": "Caminhada Meditativa na Floresta", "desc": "Olga Belyakova | Plantar a Alma", "cat": "Viagens de Natureza"},
    {"date": "2026-07-31", "start": "10:00", "end": "12:00", "loc": "Viagens de Natureza", "title": "Tradigami: Biodiversity from Paper to Life", "desc": "Letizia Leni | NBI", "cat": "Viagens de Natureza"},
    {"date": "2026-08-01", "start": "09:30", "end": "11:30", "loc": "Viagens de Natureza", "title": "Meditação no Rio", "desc": "Francisco Salgado", "cat": "Viagens de Natureza"},
    {"date": "2026-08-01", "start": "10:00", "end": "12:00", "loc": "Viagens de Natureza", "title": "Impressões da Natureza com Tintas Naturais", "desc": "NBI - Natural Business Intelligence", "cat": "Viagens de Natureza"},
    {"date": "2026-08-02", "start": "10:00", "end": "12:00", "loc": "Viagens de Natureza", "title": "Do Prado ao Prato: As Plantas Nossas Amigas", "desc": "Paulo Pereira (NBI), João Malva (CHANGEING) e Anabela Marisa Azul (PAS-GRAS)", "cat": "Viagens de Natureza"},

    # PAGE 4: VIAGENS DE TRADIÇÃO
    {"date": "2026-07-31", "start": "09:00", "end": "12:00", "loc": "Viagens de Tradição", "title": "Etnografia e Canto Polifónico | Manhouce", "desc": "Freguesia de Manhouce e Vozes de Manhouce. Custo: 12,50€", "cat": "Viagens de Tradição"},
    {"date": "2026-08-01", "start": "09:00", "end": "12:00", "loc": "Viagens de Tradição", "title": "Água Quente e Vinho Termas e Comenda", "desc": "Termalistur, Museu Romano e Quinta do Gato. Custo: 12,50€", "cat": "Viagens de Tradição"},
    {"date": "2026-08-02", "start": "09:00", "end": "12:00", "loc": "Viagens de Tradição", "title": "A Serra da Arada e a Broa Trilho dos Incas e Candal", "desc": "CLDS São Pedro do Sul, Ana Martins e Custódia Oliveira. Custo: 12,50€", "cat": "Viagens de Tradição"},

    # PAGE 4: CANTINA
    {"date": "2026-08-01", "start": "10:00", "end": "19:00", "loc": "Cantina", "title": "Cantina - Changeing Excellence Hubs", "desc": "Changeing Excellence Hubs", "cat": "Cantina"},
]

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
    
    lines.append("BEGIN:VEVENT")
    lines.append(f"UID:{uid}")
    lines.append(f"DTSTAMP:{dtstamp}")
    lines.append(f"DTSTART;TZID=Europe/Lisbon:{dtstart}")
    lines.append(f"DTEND;TZID=Europe/Lisbon:{dtend}")
    lines.append(f"SUMMARY:{ev['title']}")
    lines.append(f"DESCRIPTION:{ev['desc']}")
    lines.append(f"LOCATION:{ev['loc']}, Tradidanças (São Pedro do Sul)")
    lines.append(f"CATEGORIES:{ev['cat']}")
    lines.append("END:VEVENT")

lines.append("END:VCALENDAR")

ics_content = "\r\n".join(lines) + "\r\n"

with open("tradidancas2026.ics", "w", encoding="utf-8") as f:
    f.write(ics_content)

print(f"Generated tradidancas2026.ics with {len(events)} events.")
