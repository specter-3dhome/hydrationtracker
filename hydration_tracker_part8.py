# === Stage 8: Текстовый поиск ===
# Project: HydrationTracker
from difflib import SequenceMatcher


def build_water_drink_search(text, drinks):
    """Возвращает список напитков, чьё название содержит текст (без учёта регистра)."""
    text = text.lower().strip()
    return [drink for drink in drinks if text in drink['name'].lower()]


def find_and_highlight_drinks(text, drinks):
    """
    Находит напитки по названию и возвращает строку с выделением совпадений.

    Совпадения в названии подсветятся квадратными скобками, например:
    [Кофе] 200 мл 09:15 обычный
    """
    text = text.lower().strip()
    if not text:
        return "Поиск по пустой строке не выполнен"

    matches = build_water_drink_search(text, drinks)
    if not matches:
        return "Ничего не найдено по запросу: " + text

    parts = []
    for drink in matches:
        name = drink['name']
        name_lower = name.lower()
        if text in name_lower:
            name = '[' + name + ']'
        line = f"{name} {drink.get('volume', '')} {drink.get('time', '')} {drink.get('type', '')}"
        parts.append(line)

    return "\n".join(parts)
