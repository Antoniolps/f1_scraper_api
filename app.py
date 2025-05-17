from flask import Flask, request, jsonify
from scraper import get_race_results

app = Flask(__name__)

LAST_RACE: dict | None = None


@app.route("/race", methods=["POST"])
def load_race():
    data = request.get_json() or {}
    gp = data.get("gp")
    year = data.get("year")

    if not gp or not year:
        return jsonify({"erro": "Parametros 'gp' e 'year' são obrigatórios."}), 400

    try:
        year = int(year)
    except ValueError:
        return jsonify({"erro": "Year precisa ser inteiro."}), 400

    race = get_race_results(gp, year)
    if not race:
        return jsonify({"erro": "GP não encontrado para o ano informado."}), 404

    if "erro" in race:
        return jsonify(race), 404

    global LAST_RACE
    LAST_RACE = race
    return jsonify({"mensagem": f"{race['grand_prix']} {year} carregado com sucesso."})



def _require_race_loaded():
    if not LAST_RACE:
        return jsonify({"erro": "Nenhuma corrida carregada. Faça POST /corrida primeiro."}), 400
    return None


@app.route("/race/pole")
def pole():
    erro = _require_race_loaded()
    if erro:
        return erro
    return jsonify({"pole": LAST_RACE["pole"]})


@app.route("/race/fastest-lap")
def fastest_lap():
    erro = _require_race_loaded()
    if erro:
        return erro
    return jsonify({"fastest_lap": LAST_RACE["fastest_lap"]})


@app.route("/race/winner")
def winner():
    erro = _require_race_loaded()
    if erro:
        return erro
    return jsonify({"winner": LAST_RACE["winner"]})


@app.route("/race/team")
def team():
    erro = _require_race_loaded()
    if erro:
        return erro
    return jsonify({"team": LAST_RACE["team"]})


if __name__ == "__main__":
    app.run(debug=True)
