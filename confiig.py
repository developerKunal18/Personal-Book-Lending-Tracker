from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

BOOKS_FILE = DATA_DIR / "books.json"
LENDING_FILE = DATA_DIR / "lending_records.json"

DATE_FORMAT = "%Y-%m-%d"
DEFAULT_LOAN_DAYS = 14
