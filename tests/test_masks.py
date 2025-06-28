import pytest
from src.mask import get_mask_card_number, get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    """Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"
    assert get_mask_card_number("1234 5678 1234 5678") == "1234 56** **** 5678"  # С пробелами
    assert get_mask_card_number("123456781234567") == "1234 56** ***4 567"  # Неполный номер
    assert get_mask_card_number("12345678123456") == "1234 56** ***4 56" # Еще короче

def test_get_mask_account():
    """Тестирование правильности маскирования номера счета."""
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("1234") == "**1234"
    with pytest.raises(ValueError):
        get_mask_account("123")  # Слишком короткий номер


