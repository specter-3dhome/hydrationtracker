# === Stage 7: Фильтрация записей ===
# Project: HydrationTracker
from datetime import datetime


def _parse_volume(value):
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().lower().replace("мл", "").replace("л", "")
    for symbol in ("мл", "л", "milli", "litre", "liter"):
        text = text.replace(symbol, "")
    try:
        return float(text)
    except ValueError:
        return float("nan")


def _coerce_date(value):
    if isinstance(value, datetime):
        return value
    text = str(value).strip()
    for layout in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(text, layout)
        except ValueError:
            continue
    return datetime.fromisoformat(text)


def filter_by_volume(records, min_volume=None, max_volume=None):
    min_volume = _parse_volume(min_volume) if min_volume is not None else None
    max_volume = _parse_volume(max_volume) if max_volume is not None else None
    result = []
    for record in records:
        volume = _parse_volume(record.get("volume"))
        if min_volume is not None and volume < min_volume:
            continue
        if max_volume is not None and volume > max_volume:
            continue
        result.append(record)
    return result


def filter_by_date_range(records, start_date=None, end_date=None):
    start_date = _coerce_date(start_date) if start_date is not None else None
    end_date = _coerce_date(end_date) if end_date is not None else None
    result = []
    for record in records:
        created = _coerce_date(record.get("created_at"))
        if start_date is not None and created < start_date:
            continue
        if end_date is not None and created > end_date:
            continue
        result.append(record)
    return result


def filter_records(records, min_volume=None, max_volume=None,
                   start_date=None, end_date=None):
    records = filter_by_volume(records, min_volume, max_volume)
    records = filter_by_date_range(records, start_date, end_date)
    return records
