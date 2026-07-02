import requests
from langchain_core.tools import tool
from Tools.currency.tools.schemas import ConvertCurrencyArgs


@tool(
    "convert_currency",
    args_schema=ConvertCurrencyArgs,
    description="Конвертирует сумму из одной валюты в другую по текущему курсу.")
def convert_currency(amount: float, from_currency: str,  to_currency: str) -> float | str:
    """
    Конвертирует заданную сумму из одной валюты в другую по актуальному курсу.
    """
    print("convert_currency")
    try:
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
    except requests.RequestException:
        return "Ошибка соединения с сервисом"

    rate = response.json()["rates"][to_currency]
    result = amount * rate
    return round(result, 2)


@tool
def iphone_price() -> float:
    """
    Возвращает стоимость одного iPhone в рублях.
    """
    print("iphone_price")
    return 85_000.


if __name__ == "__main__":
    print(convert_currency.invoke({
        "amount": 100,
        "from_currency": "USD",
        "to_currency": "RUB"
    }))
