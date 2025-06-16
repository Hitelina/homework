from typing import List, Dict, Union


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, содержащий только те, у которых 'state' соответствует указанному значению.
    """
    return [item for item in data if item.get('state') == state]