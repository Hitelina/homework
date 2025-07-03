import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("счет 73654108430135874305", "счет **4305"),  # Нижний регистр
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79 ** **** 6361"),
        (
            "Mastercard Gold 5100523456789012",
            "Mastercard Gold 5100 52 ** **** 9012",
        ),  # Другой тип карты
    ],
)
def test_mask_account_card_parametrized(
    input_string: str, expected_output: str
) -> None:
    """Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции."""
    assert mask_account_card(input_string) == expected_output


def test_mask_account_card_card() -> None:
    """Тест маскировки карты."""
    assert (
        mask_account_card("Visa Platinum 7000792289606361")
        == "Visa Platinum 7000 79** **** 6361"
    )


def test_mask_account_card_invalid_input() -> None:
    """Тест на некорректный ввод, вызывающий ValueError."""
    with pytest.raises(ValueError) as excinfo:
        mask_account_card("Invalid")
    assert str(excinfo.value) == "Некорректный формат строки. Ожидается тип и номер."


def test_get_date() -> None:
    """Тест преобразования даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2023-12-31T23:59:59") == "31.12.2023"  # Другой формат
