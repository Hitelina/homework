from src.mask import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(info: str) -> str:
    """
    Обрабатывает строку с типом и номером, возвращает строку с типом и маскированным номером.
    """
    parts: list[str] = info.strip().split()
    if len(parts) < 2:
        raise ValueError("Некорректный формат строки. Ожидается тип и номер.")

    number: str = parts[-1]
    type_str: str = " ".join(parts[:-1])  # сохраняем оригинальный регистр для вывода
    type_str_lower: str = type_str.lower()

    if "счет" in type_str_lower:
        masked_number: str = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{type_str} {masked_number}"


print(mask_account_card("Visa Platinum 7000792289606361"))


def get_date(date_str: str) -> str:
    """
    Принимает строку с датой в формате ISO 8601 и возвращает строку в формате ДД.ММ.ГГГГ.

    :param date_str: str, дата в формате "2024-03-11T02:26:18.671407"
    :return: str, дата в формате "11.03.2024"
    """
    # Парсим строку в объект datetime
    dt = datetime.fromisoformat(date_str)
    # Форматируем дату в нужный формат
    return dt.strftime("%d.%m.%Y")
