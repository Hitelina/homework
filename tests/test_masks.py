import pytest
from src.mask import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    """Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"
    assert (
        get_mask_card_number("1234 5678 1234 5678") == "1234 56** **** 5678"
    )  # С пробелами


def test_get_mask_account():
    """Тестирование правильности маскирования номера счета."""
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("1234") == "**1234"
    with pytest.raises(ValueError):
        get_mask_account("123")  # Слишком короткий номер
