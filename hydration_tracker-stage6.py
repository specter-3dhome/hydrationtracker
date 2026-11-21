# === Stage 6: Связи между сущностями ===
# Project: HydrationTracker
from datetime import datetime


class Beverage:
    def __init__(self, name, volume, drink_type):
        self.name = name
        self.volume = volume
        self.drink_type = drink_type
        self.records = []

    def __repr__(self):
        return f"Beverage(name={self.name!r}, volume={self.volume}, drink_type={self.drink_type!r})"


class Record:
    def __init__(self, beverage, volume, time):
        self.beverage = beverage
        self.volume = volume
        self.time = time

    def __repr__(self):
        return f"Record(beverage={self.beverage.name!r}, volume={self.volume}, time={self.time!r})"


def get_beverage_by_name(beverages, name):
    for beverage in beverages:
        if beverage.name == name:
            return beverage
    return None


def add_record(beverage, volume, time):
    record = Record(beverage, volume, time)
    beverage.records.append(record)
    return record


def get_all_records_for_beverage(beverages, beverage):
    return beverage.records


def check_integrity(beverages):
    beverage_names = [beverage.name for beverage in beverages]
    for beverage in beverages:
        for record in beverage.records:
            if record.beverage.name not in beverage_names:
                return False, f"Связь нарушена: запись относится к несуществующему напитку {record.beverage.name!r}"
            if record.time is None:
                return False, f"Связь нарушена: запись {record.volume} мл без времени"
            if record.volume <= 0:
                return False, f"Связь нарушена: запись {record.volume} мл с некорректным объёмом"
    return True, "Целостность проверена"
