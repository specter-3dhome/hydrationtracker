# === Stage 9: Поиск по нескольким словам ===
# Project: HydrationTracker
import re
from dataclasses import dataclass, field
from typing import List, Dict, Iterable, Set, Optional


@dataclass
class Drink:
    name: str
    volume: float
    time: str
    kind: str


class HydrationSearch:
    def __init__(self, drinks: Iterable[Drink]):
        self._by_name: Dict[str, Drink] = {}
        self._by_time: Dict[str, Drink] = {}
        self._by_kind: Dict[str, Drink] = {}
        for drink in drinks:
            self._by_name[drink.name.lower()] = drink
            self._by_time[drink.time.lower()] = drink
            self._by_kind[drink.kind.lower()] = drink

    def search(self, query: str) -> List[Drink]:
        return list(self._matches(query))

    def _matches(self, query: str) -> Iterable[Drink]:
        query = query.strip()
        if not query:
            return

        tokens = self._split_tokens(query)
        if not tokens:
            return

        must: Set[str] = set()
        exclude: Set[str] = set()
        for token in tokens:
            if token.startswith("-"):
                exclude.add(token[1:].strip().lower())
            else:
                must.add(token.strip().lower())

        if not must and not exclude:
            return

        candidates = self._all_drinks()
        if exclude:
            candidates = [d for d in candidates if not self._hits_any(d, exclude)]
        if must:
            candidates = [d for d in candidates if self._hits_any(d, must)]

        return candidates

    def _all_drinks(self) -> List[Drink]:
        seen: List[Drink] = []
        for source in (self._by_name, self._by_time, self._by_kind):
            for drink in source.values():
                if drink not in seen:
                    seen.append(drink)
        return seen

    def _hits_any(self, drink: Drink, terms: Set[str]) -> bool:
        haystack = self._search_fields(drink)
        return any(term in haystack for term in terms)

    @staticmethod
    def _search_fields(drink: Drink) -> str:
        return " ".join(
            field_value.lower()
            for field_value in (
                drink.name,
                drink.volume,
                drink.time,
                drink.kind,
            )
        )

    @staticmethod
    def _split_tokens(query: str) -> List[str]:
        pattern = r"(?:^|\s)(-)?([^\s]+)(?=\s|$)"
        matches = re.findall(pattern, query)
        return [
            token
            for _, excluded, token in matches
            if not (excluded and token == "")
        ]
