from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(info):
    """
    Обрабатывает строку с типом и номером, возвращает строку с типом и маскированным номером.
    """
    parts = info.strip().split()
    if len(parts) < 2:
        raise ValueError("Некорректный формат строки. Ожидается тип и номер.")

    number = parts[-1]
    type_str = " ".join(parts[:-1])  # сохраняем оригинальный регистр для вывода
    type_str_lower = type_str.lower()

    if "счет" in type_str_lower:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{type_str} {masked_number}"

print(mask_account_card("Visa Platinum 7000792289606361"))