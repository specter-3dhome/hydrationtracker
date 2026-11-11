# === Stage 2: Проверка полей ===
# Project: HydrationTracker
import datetime


class Beverage:
    def __init__(self, name, volume, time, type):
        self.name = name
        self.volume = volume
        self.time = time
        self.type = type

    def validate(self):
        errors = []
        if not isinstance(self.name, str) or not self.name.strip():
            errors.append("Название напитка обязательно и должно быть строкой.")
        if not isinstance(self.volume, (int, float)) or self.volume <= 0:
            errors.append("Объём должен быть положительным числом.")
        if not isinstance(self.time, datetime.time):
            errors.append("Время должно быть объектом типа datetime.time.")
        if not isinstance(self.type, str) or not self.type.strip():
            errors.append("Тип напитка обязателен и должен быть строкой.")
        return errors

    def __str__(self):
        return f"{self.name}, {self.volume} мл, {self.time}, {self.type}"


def normalize_volume(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def normalize_time(value):
    if isinstance(value, datetime.time):
        return value
    parts = str(value).split(":")
    if len(parts) == 2:
        try:
            return datetime.time(int(parts[0]), int(parts[1]))
        except ValueError:
            return None
    return None


def normalize_type(value):
    types = {"вода", "чай", "кофе", "сок", "молоко", "лимонад", "другое"}
    if value in types:
        return value
    return None


def normalize_name(value):
    return value.strip().title()


def parse_beverage_input(name, volume, time, type):
    beverage = Beverage(name, volume, time, type)
    errors = beverage.validate()
    if errors:
        return None, errors
    return beverage, []
