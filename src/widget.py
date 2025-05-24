from src.mask import get_mask_account, get_mask_card_number

def mask_account_card():
    """
    Обрабатывает строку с типом и номером, возвращает маскированный номер.

    :param info: str, например "Visa Platinum 7000792289606361"
    :return: str, маскированный номер
    """
    # Разделение строки по пробелам
    parts = info.strip().split()

    # Проверка, что строка содержит минимум 2 части
    if len(parts) < 2:
        raise ValueError("Некорректный формат строки. Ожидается тип и номер.")

    # Тип — все части, кроме последней (например, "Visa Platinum" или "Счет")
    # Номер — последний элемент
    *types, number = parts
    type_str = " ".join(types)

    # Обработка по типу
    if type_str.lower() in ["счет", " счет"]:
        # Маскируем счет
        masked_number = get_mask_account(number)
    else:
        # Маскируем карту
        masked_number = get_mask_card(number)

    return masked_number