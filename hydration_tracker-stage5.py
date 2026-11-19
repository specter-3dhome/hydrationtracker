# === Stage 5: Удаление и восстановление ===
# Project: HydrationTracker
import datetime


class SoftDeletedBeverage:
    """Напиток с возможностью мягкого удаления и восстановления."""

    def __init__(self, name, volume, time, drink_type):
        self.name = name
        self.volume = volume
        self.time = time
        self.drink_type = drink_type
        self.deleted = False
        self.deleted_at = None

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = datetime.datetime.now()

    def restore(self):
        self.deleted = False
        self.deleted_at = None

    def is_deleted(self):
        return self.deleted

    def to_dict(self):
        return {
            "name": self.name,
            "volume": self.volume,
            "time": self.time,
            "drink_type": self.drink_type,
            "deleted": self.deleted,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
        }


class BeverageStore:
    """Хранилище напитков с поддержкой мягкого удаления."""

    def __init__(self):
        self._items = {}

    def add(self, beverage):
        self._items[beverage.name] = beverage

    def get(self, name):
        return self._items.get(name)

    def list_active(self):
        return [b for b in self._items.values() if not b.is_deleted()]

    def list_deleted(self):
        return [b for b in self._items.values() if b.is_deleted()]

    def soft_delete(self, name):
        beverage = self.get(name)
        if beverage:
            beverage.soft_delete()

    def restore(self, name):
        beverage = self.get(name)
        if beverage and beverage.is_deleted():
            beverage.restore()

    def remove(self, name):
        self._items.pop(name, None)
