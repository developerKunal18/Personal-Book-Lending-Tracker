import json
from config import DATA_DIR, BOOKS_FILE, LENDING_FILE


def initialize_storage():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for file_path in (BOOKS_FILE, LENDING_FILE):
        if not file_path.exists():
            with file_path.open("w", encoding="utf-8") as file:
                json.dump([], file, indent=4)


def load_data(file_path):
    initialize_storage()

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        print(f"Warning: Invalid data format in {file_path.name}.")
        return []

    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not read {file_path.name}: {error}")
        return []


def save_data(file_path, data):
    initialize_storage()

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_books():
    return load_data(BOOKS_FILE)


def save_books(books):
    save_data(BOOKS_FILE, books)


def load_lending_records():
    return load_data(LENDING_FILE)


def save_lending_records(records):
    save_data(LENDING_FILE, records)
