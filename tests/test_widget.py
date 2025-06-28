import pytest
from src.widget import mask_account_card, get_date
from src.mask import get_mask_account, get_mask_card_number  # Импортируем для мок-тестов


def test_mask_account_card_account():
    """Тест маскировки счета."""
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("счет 73654108430135874305") == "счет **4305"  # Нижний регистр


def test_mask_account_card_card():
    """Тест маскировки карты."""
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_invalid_input():
    """Тест на некорректный ввод, вызывающий ValueError."""
    with pytest.raises(ValueError) as excinfo:
        mask_account_card("Invalid")
    assert str(excinfo.value) == "Некорректный формат строки. Ожидается тип и номер."


def test_get_date():
    """Тест преобразования даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2023-12-31T23:59:59") == "31.12.2023"  # Другой формат