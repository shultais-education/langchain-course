import requests
from langchain_core.tools import tool


@tool("convert_currency", parse_docstring=True)
def convert_currency(amount: float | int, from_currency: str,  to_currency: str) -> float:
    """
    Конвертирует заданную сумму из одной валюты в другую по актуальному курсу.

    Args:
        amount: Сумма для конвертации (целое или вещественное число).
        from_currency: Трехбуквенный код исходной валюты в стандарте ISO 4217 (например, 'USD', 'EUR', 'RUB').
        to_currency: Трехбуквенный код целевой валюты в стандарте ISO 4217 (например, 'USD', 'EUR', 'RUB').

    Returns:
        float: Сконвертированная сумма, округлённая до двух знаков после запятой.
    """
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
    rate = response.json()["rates"][to_currency]
    result = amount * rate
    return round(result, 2)


if __name__ == "__main__":
    print(convert_currency.invoke({
        "amount": 100,
        "from_currency": "USD",
        "to_currency": "RUB"
    }))
