# === Stage 3: Хранилище в памяти ===
# Project: HydrationTracker
from datetime import datetime


class Beverage:
    def __init__(self, name, volume, time, type_):
        self.id = None
        self.name = name
        self.volume = volume
        self.time = time
        self.type = type_

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "volume": self.volume,
            "time": self.time,
            "type": self.type,
        }

    def __repr__(self):
        return f"Beverage(id={self.id!r}, name={self.name!r}, volume={self.volume!r}, time={self.time!r}, type={self.type!r})"


class BeverageStore:
    def __init__(self):
        self._items = {}

    def add(self, beverage):
        beverage.id = self._generate_id()
        self._items[beverage.id] = beverage
        return beverage

    def get(self, beverage_id):
        return self._items.get(beverage_id)

    def list(self):
        return list(self._items.values())

    def _generate_id(self):
        counter = self._items
        for candidate in range(1, len(counter) + 1):
            if candidate not in counter:
                return candidate
        return len(counter) + 1


def load_sample_data(store):
    store.add(Beverage("Вода", 250, "08:00", "безалкогольный"))
    store.add(Beverage("Чай", 200, "10:30", "напиток"))
    store.add(Beverage("Кофе", 150, "14:00", "напиток"))


if __name__ == "__main__":
    store = BeverageStore()
    load_sample_data(store)

    for beverage in store.list():
        print(beverage)

    print(store.get(2))
