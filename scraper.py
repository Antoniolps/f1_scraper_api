import requests
from bs4 import BeautifulSoup
from gp_mapper import map_gp_to_official_name


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

    # Build a mapping from header name to column index
    col_map = {name: idx for idx, name in enumerate(header_texts)}

    lines_gp = []
    for row in table.find_all("tr")[1:]:  # skip header
        cols = row.find_all(["td", "th"])
        if len(cols) < len(col_map):
            continue
        # Find the column index for 'grand prix' (fuzzy, ignoring footnotes)
        gp_col_idx = next((idx for name, idx in col_map.items() if "grand prix" in name), None)

        lines_gp.append(
            {
                "grand_prix": cols[gp_col_idx].get_text(strip=True) if gp_col_idx is not None else None,
                "pole": cols[col_map.get("pole position")].get_text(strip=True) if "pole position" in col_map else None,
                "fastest_lap": cols[col_map.get("fastest lap")].get_text(strip=True) if "fastest lap" in col_map else None,
                "winner": cols[col_map.get("winning driver")].get_text(strip=True) if "winning driver" in col_map else None,
                "team": cols[col_map.get("winning constructor")].get_text(strip=True) if "winning constructor" in col_map else None,
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