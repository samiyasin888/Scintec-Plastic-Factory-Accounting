from pathlib import Path

APP_NAME = "Global"
APP_VERSION = "1.0.0"
APP_COMPANY = "Scintec Plastic Factory"
DEFAULT_LANGUAGE = "en"
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "global.db"

DATA_DIR.mkdir(exist_ok=True)
