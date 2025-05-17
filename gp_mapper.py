def map_gp_to_official_name(gp: str) -> str:
    gp_map = {
        # Bahrain
        "bahrein": "Bahrain Grand Prix",
        "bahrain": "Bahrain Grand Prix",
        "sakhir": "Bahrain Grand Prix",
        # Saudi Arabia
        "arábia saudita": "Saudi Arabian Grand Prix",
        "arabia saudita": "Saudi Arabian Grand Prix",
        "saudi arabia": "Saudi Arabian Grand Prix",
        "jeddah": "Saudi Arabian Grand Prix",
        # Australia
        "austrália": "Australian Grand Prix",
        "australia": "Australian Grand Prix",
        "melbourne": "Australian Grand Prix",
        # Japan
        "japão": "Japanese Grand Prix",
        "japao": "Japanese Grand Prix",
        "japan": "Japanese Grand Prix",
        "suzuka": "Japanese Grand Prix",
        # China
        "china": "Chinese Grand Prix",
        "xangai": "Chinese Grand Prix",
        "shanghai": "Chinese Grand Prix",
        # Miami
        "miami": "Miami Grand Prix",
        # Emilia Romagna
        "emilia-romagna": "Emilia Romagna Grand Prix",
        "emilia romagna": "Emilia Romagna Grand Prix",
        "imola": "Emilia Romagna Grand Prix",
        # Monaco
        "mônaco": "Monaco Grand Prix",
        "monaco": "Monaco Grand Prix",
        # Canada
        "canadá": "Canadian Grand Prix",
        "canada": "Canadian Grand Prix",
        "montreal": "Canadian Grand Prix",
        # Spain
        "espanha": "Spanish Grand Prix",
        "espanol": "Spanish Grand Prix",
        "spain": "Spanish Grand Prix",
        "barcelona": "Spanish Grand Prix",
        # Austria
        "áustria": "Austrian Grand Prix",
        "austria": "Austrian Grand Prix",
        "spielberg": "Austrian Grand Prix",
        # UK
        "reino unido": "British Grand Prix",
        "inglaterra": "British Grand Prix",
        "britain": "British Grand Prix",
        "british": "British Grand Prix",
        "silverstone": "British Grand Prix",
        # Hungary
        "hungria": "Hungarian Grand Prix",
        "hungary": "Hungarian Grand Prix",
        "mogyorod": "Hungarian Grand Prix",
        # Belgium
        "bélgica": "Belgian Grand Prix",
        "belgica": "Belgian Grand Prix",
        "belgium": "Belgian Grand Prix",
        "spa": "Belgian Grand Prix",
        # Netherlands
        "holanda": "Dutch Grand Prix",
        "países baixos": "Dutch Grand Prix",
        "paises baixos": "Dutch Grand Prix",
        "netherlands": "Dutch Grand Prix",
        "zandvoort": "Dutch Grand Prix",
        # Italy
        "itália": "Italian Grand Prix",
        "italia": "Italian Grand Prix",
        "italy": "Italian Grand Prix",
        "monza": "Italian Grand Prix",
        # Azerbaijan
        "azerbaijão": "Azerbaijan Grand Prix",
        "azerbaijao": "Azerbaijan Grand Prix",
        "azerbaijan": "Azerbaijan Grand Prix",
        "baku": "Azerbaijan Grand Prix",
        # Singapore
        "singapura": "Singapore Grand Prix",
        "singapore": "Singapore Grand Prix",
        # USA
        "estados unidos": "United States Grand Prix",
        "eua": "United States Grand Prix",
        "usa": "United States Grand Prix",
        "austin": "United States Grand Prix",
        # Mexico
        "méxico": "Mexico City Grand Prix",
        "mexico": "Mexico City Grand Prix",
        # Brazil
        "brasil": "São Paulo Grand Prix",
        "são paulo": "São Paulo Grand Prix",
        "sao paulo": "São Paulo Grand Prix",
        "interlagos": "São Paulo Grand Prix",
        # Las Vegas
        "las vegas": "Las Vegas Grand Prix",
        # Qatar
        "catar": "Qatar Grand Prix",
        "qatar": "Qatar Grand Prix",
        "lusail": "Qatar Grand Prix",
        # Abu Dhabi
        "abu dhabi": "Abu Dhabi Grand Prix",
        "yas marina": "Abu Dhabi Grand Prix",
    }

    return gp_map.get(gp.lower(), None)