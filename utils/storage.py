import json
import os

DATA_FILE = "data/counter.json"


def load_count():
    if not os.path.exists(DATA_FILE):
        save_count(0)
        return 0

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("count", 0)
    except Exception:
        save_count(0)
        return 0


def save_count(count):
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            {"count": count},
            file,
            ensure_ascii=False,
            indent=4
        )