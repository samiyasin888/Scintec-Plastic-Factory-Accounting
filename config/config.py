import os
from pathlib import Path

APP_NAME = "Global"
APP_VERSION = "1.0.0"
APP_COMPANY = "Scintec Plastic Factory"
DEFAULT_LANGUAGE = "en"

# Use a stable, user-specific folder for runtime data.
# This is important for packaged desktop builds so the database and generated files
# are stored in the user's AppData on Windows instead of the temporary PyInstaller folder.
if os.name == "nt":
    base_dir = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
else:
    base_dir = Path.home() / ".global_accounting"

DATA_DIR = base_dir / "GlobalAccounting"
DB_PATH = DATA_DIR / "global.db"
DATA_DIR.mkdir(parents=True, exist_ok=True)
