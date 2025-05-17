Certainly! Here’s a professional and informative `README.MD` for your F1 API project:

---

# 🏎️ F1 API

A Python Flask API to fetch and serve Formula 1 Grand Prix results and schedule data directly from Wikipedia, supporting flexible Grand Prix name mapping and robust scraping for multiple seasons.

---

## 🚀 Features

- **Get Race Results:** Retrieve pole position, fastest lap, winner, and winning constructor for any Grand Prix and year.
- **Flexible GP Name Mapping:** Accepts various aliases and languages for Grand Prix names (e.g., "brasil", "São Paulo", "Brazil", etc.).
- **Automatic Wikipedia Scraping:** Always up-to-date with the latest F1 data, directly from Wikipedia.
- **Graceful Handling:** Returns clear error messages if results are not yet available or if the GP is not found.
- **Caching:** Reduces repeated requests for the same season.

---

## 📦 Endpoints

### `POST /race`
Load a specific Grand Prix for a given year.

**Request JSON:**
```json
{
  "gp": "brasil",
  "year": 2024
}
```

**Response:**
- `{"mensagem": "São Paulo Grand Prix 2024 carregado com sucesso."}`
- Or error: `{"erro": "GP não encontrado para o ano informado."}`

---

### `GET /race/pole`
Returns the pole position driver for the loaded race.

### `GET /race/fastest-lap`
Returns the fastest lap driver for the loaded race.

### `GET /race/winner`
Returns the winner of the loaded race.

### `GET /race/team`
Returns the winning constructor/team for the loaded race.

---

## 🛠️ How It Works

- Uses `requests` and `BeautifulSoup` to scrape the relevant Wikipedia page for the given year.
- Dynamically finds and parses the results table, handling changes in column order and footnote legends.
- Cleans up all values to remove Wikipedia footnote references.
- Maps user input to official Grand Prix names using a robust mapping dictionary.

---

## 🏁 Example Usage

```bash
curl -X POST http://localhost:5000/race -H "Content-Type: application/json" -d '{"gp": "brasil", "year": 2024}'
curl http://localhost:5000/race/winner
```

---

## 🧩 Requirements

- Python 3.10+
- Flask
- requests
- beautifulsoup4

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📚 Project Structure

```
.
├── app.py           # Flask API endpoints
├── scraper.py       # Wikipedia scraping and data extraction
├── gp_mapper.py     # Grand Prix name mapping logic
└── README.MD        # This file
```

---

## 🌍 Data Source

All data is sourced live from [Wikipedia - Formula One World Championship](https://en.wikipedia.org/wiki/Formula_One_World_Championship).
