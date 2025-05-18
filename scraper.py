import requests
from bs4 import BeautifulSoup
from gp_mapper import map_gp_to_official_name
import re


CACHE_SEASONS: dict[int, list[dict]] = {}


def _scrape_tabela_temporada(year: int):
    if year in CACHE_SEASONS:
        return CACHE_SEASONS[year]

    url = f"https://en.wikipedia.org/wiki/{year}_Formula_One_World_Championship"
    result = requests.get(url, timeout=15)
    result.raise_for_status()
    soup = BeautifulSoup(result.text, "html.parser")

    table = None

    for tbl in soup.find_all("table", class_=lambda c: c and "wikitable" in c):
        header_texts = [th.get_text(strip=True).lower() for th in tbl.find_all("th")]
        if "pole position" in header_texts and "fastest lap" in header_texts and "winning driver" in header_texts and "winning constructor" in header_texts:
            table = tbl
            break

    if not table:
        raise ValueError("Tabela de Grands Prix não encontrada para o ano informado.")

    
    header_row = table.find("tr")
    header_texts = [th.get_text(strip=True).lower() for th in header_row.find_all("th")]

    col_map = {name: idx for idx, name in enumerate(header_texts)}

    lines_gp = []
    for row in table.find_all("tr")[1:]:  
        cols = row.find_all(["td", "th"])
        if len(cols) < len(col_map):
            continue
        
        gp_col_idx = next((idx for name, idx in col_map.items() if "grand prix" in name), None)
        pole_col_idx = next((idx for name, idx in col_map.items() if "pole position" in name), None)
        fastest_lap_col_idx = next((idx for name, idx in col_map.items() if "fastest lap" in name), None)
        winner_col_idx = next((idx for name, idx in col_map.items() if "winning driver" in name), None)
        team_col_idx = next((idx for name, idx in col_map.items() if "winning constructor" in name), None)

        lines_gp.append(
            {
                "grand_prix": clean_value(cols[gp_col_idx].get_text(strip=True)) if gp_col_idx is not None else None,
                "pole": clean_value(cols[pole_col_idx].get_text(strip=True)) if pole_col_idx is not None else None,
                "fastest_lap": clean_value(cols[fastest_lap_col_idx].get_text(strip=True)) if fastest_lap_col_idx is not None else None,
                "winner": clean_value(cols[winner_col_idx].get_text(strip=True)) if winner_col_idx is not None else None,
                "team": clean_value(cols[team_col_idx].get_text(strip=True)) if team_col_idx is not None else None,
            }
        )

    CACHE_SEASONS[year] = lines_gp
    return lines_gp


def get_race_results(gp: str, year: int) -> dict | None:
    official_name = map_gp_to_official_name(gp)
    if not official_name:
        return None

    season = _scrape_tabela_temporada(year)
    for race in season:
        if race["grand_prix"].lower() == official_name.lower():
            if not race["winner"]:
                return {"erro": f"Resultados não disponíveis para {official_name} {year}."}
            return race
    return None


def clean_value(val: str) -> str:
    # Remove bracketed references like [c], [12], [note 1], etc.
    return re.sub(r'\[[^\]]*\]', '', val).strip()