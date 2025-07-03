import pytest
from src.processing import filter_by_state, sort_by_date
from typing import List, Dict, Any

# Фикстуры для тестовых данных


@pytest.fixture
def test_data() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 123456789, "state": "PENDING", "date": "2019-01-01T00:00:00.000000"},
    ]


def test_filter_by_state_executed(test_data: List[Dict]) -> None:
    """Тестирование фильтрации по статусу 'EXECUTED'."""
    filtered_data = filter_by_state(test_data, state="EXECUTED")
    assert len(filtered_data) == 2
    for item in filtered_data:
        assert item["state"] == "EXECUTED"


def test_filter_by_state_canceled(test_data: List[Dict]) -> None:
    """Тестирование фильтрации по статусу 'CANCELED'."""
    filtered_data = filter_by_state(test_data, state="CANCELED")
    assert len(filtered_data) == 2
    for item in filtered_data:
        assert item["state"] == "CANCELED"


def test_filter_by_state_no_match(test_data: List[Dict]) -> None:
    """Тестирование фильтрации, когда нет совпадений."""
    filtered_data = filter_by_state(test_data, state="UNKNOWN")
    assert len(filtered_data) == 0


def test_sort_by_date_ascending(test_data: List[Dict]) -> None:
    """Тестирование сортировки по дате в возрастающем порядке."""
    sorted_data = sort_by_date(test_data, reverse=False)
    dates = [item["date"] for item in sorted_data]
    assert dates == sorted(dates)  # Проверяем, что даты отсортированы


def test_sort_by_date_descending(test_data: List[Dict]) -> None:
    """Тестирование сортировки по дате в убывающем порядке."""
    sorted_data = sort_by_date(test_data, reverse=True)
    dates = [item["date"] for item in sorted_data]
    assert dates == sorted(
        dates, reverse=True
    )  # Проверяем, что даты отсортированы в обратном порядке
