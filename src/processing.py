from datetime import datetime
from typing import List, Dict, Union


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, содержащий только те, у которых 'state' соответствует указанному значению.
    """
    return [item for item in data if item.get('state') == state]

def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате (ключ 'date').

    :param data: Список словарей.
    :param reverse: Порядок сортировки (True - убывание, False - возрастание, по умолчанию True).
    :return: Новый список, отсортированный по дате.
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)