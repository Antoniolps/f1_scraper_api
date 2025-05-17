def map_gp_to_official_name(gp: str) -> str:
    gp_map = {
        # Bahrain
        "bahrain": "Bahrain Grand Prix",
        "sakhir": "Bahrain Grand Prix",
        "bahrain international circuit": "Bahrain Grand Prix",
        # Saudi Arabia
        "arábia saudita": "Saudi Arabian Grand Prix",
        "arabia saudita": "Saudi Arabian Grand Prix",
        "saudi arabia": "Saudi Arabian Grand Prix",
        "jeddah": "Saudi Arabian Grand Prix",
        "jeddah corniche circuit": "Saudi Arabian Grand Prix",
        # Australia
        "austrália": "Australian Grand Prix",
        "australia": "Australian Grand Prix",
        "melbourne": "Australian Grand Prix",
        "albert park": "Australian Grand Prix",
        "albert park circuit": "Australian Grand Prix",
        # Japan
        "japão": "Japanese Grand Prix",
        "japao": "Japanese Grand Prix",
        "japan": "Japanese Grand Prix",
        "suzuka": "Japanese Grand Prix",
        "suzuka international racing course": "Japanese Grand Prix",
        # China
        "china": "Chinese Grand Prix",
        "xangai": "Chinese Grand Prix",
        "shanghai": "Chinese Grand Prix",
        "shanghai international circuit": "Chinese Grand Prix",
        # Miami
        "miami": "Miami Grand Prix",
        "miami gardens": "Miami Grand Prix",
        "miami autodrome": "Miami Grand Prix",
        "miami international autodrome": "Miami Grand Prix",
        # Emilia Romagna
        "emilia-romagna": "Emilia Romagna Grand Prix",
        "emilia romagna": "Emilia Romagna Grand Prix",
        "imola": "Emilia Romagna Grand Prix",
        "romagna": "Emilia Romagna Grand Prix",
        "autodromo enzo e dino ferrari": "Emilia Romagna Grand Prix",
        # Monaco
        "mônaco": "Monaco Grand Prix",
        "monaco": "Monaco Grand Prix",
        "circuit de monaco": "Monaco Grand Prix",
        # Canada
        "canadá": "Canadian Grand Prix",
        "canada": "Canadian Grand Prix",
        "montreal": "Canadian Grand Prix",
        "gilles villeneuve": "Canadian Grand Prix",
        "circuit gilles villeneuve": "Canadian Grand Prix",
        # Spain
        "espanha": "Spanish Grand Prix",
        "espanol": "Spanish Grand Prix",
        "spain": "Spanish Grand Prix",
        "barcelona": "Spanish Grand Prix",
        "catalunya": "Spanish Grand Prix",
        "montmelo": "Spanish Grand Prix",
        "barcelona-catalunya": "Spanish Grand Prix",
        "circuit de barcelona-catalunya": "Spanish Grand Prix",
        # Austria
        "áustria": "Austrian Grand Prix",
        "austria": "Austrian Grand Prix",
        "spielberg": "Austrian Grand Prix",
        "red bull ring": "Austrian Grand Prix",
        # UK
        "reino unido": "British Grand Prix",
        "inglaterra": "British Grand Prix",
        "britain": "British Grand Prix",
        "british": "British Grand Prix",
        "silverstone": "British Grand Prix",
        "silverstone circuit": "British Grand Prix",
        # Hungary
        "hungria": "Hungarian Grand Prix",
        "hungary": "Hungarian Grand Prix",
        "mogyorod": "Hungarian Grand Prix",
        "hungaroring": "Hungarian Grand Prix",
        # Belgium
        "bélgica": "Belgian Grand Prix",
        "belgica": "Belgian Grand Prix",
        "belgium": "Belgian Grand Prix",
        "spa": "Belgian Grand Prix",
        "spa-francorchamps": "Belgian Grand Prix",
        "spa francorchamps": "Belgian Grand Prix",
        "circuit de spa-francorchamps": "Belgian Grand Prix",
        "stavelot": "Belgian Grand Prix",
        # Netherlands
        "holanda": "Dutch Grand Prix",
        "países baixos": "Dutch Grand Prix",
        "paises baixos": "Dutch Grand Prix",
        "netherlands": "Dutch Grand Prix",
        "zandvoort": "Dutch Grand Prix",
        "zandvoort circuit": "Dutch Grand Prix",
        "circuit zandvoort": "Dutch Grand Prix",
        # Italy
        "itália": "Italian Grand Prix",
        "italia": "Italian Grand Prix",
        "italy": "Italian Grand Prix",
        "monza": "Italian Grand Prix",
        "monza circuit": "Italian Grand Prix",
        "circuit monza": "Italian Grand Prix",
        # Azerbaijan
        "azerbaijão": "Azerbaijan Grand Prix",
        "azerbaijao": "Azerbaijan Grand Prix",
        "azerbaijan": "Azerbaijan Grand Prix",
        "baku": "Azerbaijan Grand Prix",
        "baku city circuit": "Azerbaijan Grand Prix",
        # Singapore
        "singapura": "Singapore Grand Prix",
        "singapore": "Singapore Grand Prix",
        "marina bay": "Singapore Grand Prix",
        "marina bay street circuit": "Singapore Grand Prix",
        # USA
        "estados unidos": "United States Grand Prix",
        "eua": "United States Grand Prix",
        "usa": "United States Grand Prix",
        "austin": "United States Grand Prix",
        "austin texas": "United States Grand Prix",
        "circuit of the americas": "United States Grand Prix",
        # Mexico
        "méxico": "Mexico City Grand Prix",
        "mexico": "Mexico City Grand Prix",
        "hermanos rodriguez": "Mexico City Grand Prix",
        "autódromo hermanos rodríguez": "Mexico City Grand Prix",
        "autodromo hermanos rodriguez": "Mexico City Grand Prix",
        # Brazil
        "brasil": "São Paulo Grand Prix",
        "são paulo": "São Paulo Grand Prix",
        "sao paulo": "São Paulo Grand Prix",
        "interlagos": "São Paulo Grand Prix",
        "interlagos circuit": "São Paulo Grand Prix",
        # Las Vegas
        "las vegas": "Las Vegas Grand Prix",
        "las vegas strip circuit": "Las Vegas Grand Prix",
        "paradise nevada": "Las Vegas Grand Prix",
        # Qatar
        "catar": "Qatar Grand Prix",
        "qatar": "Qatar Grand Prix",
        "lusail": "Qatar Grand Prix",
        "lusail international circuit": "Qatar Grand Prix",
        # Abu Dhabi
        "abu dhabi": "Abu Dhabi Grand Prix",
        "yas marina": "Abu Dhabi Grand Prix",
        "yas marina circuit": "Abu Dhabi Grand Prix",
    }

    return gp_map.get(gp.lower(), None)