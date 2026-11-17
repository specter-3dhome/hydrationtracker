# === Stage 4: Редактирование записей ===
# Project: HydrationTracker
from datetime import datetime


def validate_drink_update(data):
    allowed_fields = {"name", "volume", "drink_type"}
    errors = []

    for field in data:
        if field not in allowed_fields:
            errors.append(f"Поле '{field}' не допустимо для редактирования напитка")

    if "name" in data and not isinstance(data["name"], str):
        errors.append("Название напитка должно быть строкой")

    if "volume" in data:
        if not isinstance(data["volume"], (int, float)) or data["volume"] <= 0:
            errors.append("Объём напитка должен быть положительным числом")

    if "drink_type" in data and data["drink_type"] not in ("вода", "чай", "кофе", "сок", "другое"):
        errors.append("Тип напитка должен быть из допустимого списка")

    return errors


def update_drink_by_id(drinks, drink_id, data):
    for drink in drinks:
        if drink["id"] == drink_id:
            if validate_drink_update(data):
                return False
            for field, value in data.items():
                if field in drink:
                    drink[field] = value
            return True
    return False


def create_drink(drinks, name, volume, drink_type, hour=0, minute=0):
    new_id = len(drinks) + 1
    drink = {
        "id": new_id,
        "name": name,
        "volume": volume,
        "drink_type": drink_type,
        "time": f"{hour:02d}:{minute:02d}",
    }
    drinks.append(drink)
    return drink


def get_drink_by_id(drinks, drink_id):
    for drink in drinks:
        if drink["id"] == drink_id:
            return drink
    return None


def list_drinks(drinks):
    for drink in drinks:
        print(f"ID {drink['id']}: {drink['name']} ({drink['volume']} мл, {drink['drink_type']}, {drink['time']})")
