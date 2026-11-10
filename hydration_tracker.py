# === Stage 1: Каркас модуля ===
# Project: HydrationTracker
from dataclasses import dataclass, field
from datetime import time


@dataclass(frozen=True)
class Beverage:
    name: str
    volume_ml: int
    time: time
    kind: str


def make_demo_beverages() -> list[Beverage]:
    return [
        Beverage(name="Вода", volume_ml=250, time=time(8, 0), kind="вода"),
        Beverage(name="Зелёный чай", volume_ml=200, time=time(12, 30), kind="чай"),
        Beverage(name="Апельсиновый сок", volume_ml=250, time=time(15, 15), kind="сок"),
        Beverage(name="Кофе", volume_ml=150, time=time(10, 0), kind="кофе"),
    ]


def main() -> None:
    for beverage in make_demo_beverages():
        print(f"{beverage.name} — {beverage.volume_ml} мл, "
              f"{beverage.time}, тип: {beverage.kind}")
        print()


if __name__ == "__main__":
    main()
