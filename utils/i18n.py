import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_language(lang):
    file_path = BASE_DIR / "1_locales" / f"{lang}.json"

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def t(lang_dict, key):
    return lang_dict.get(key, key)
