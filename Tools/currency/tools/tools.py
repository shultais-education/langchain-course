import httpx
from datetime import datetime as dt
from langchain_core.tools import tool, BaseTool
from Tools.currency.tools.schemas import ConvertCurrencyArgs
from pydantic import BaseModel, Field
from typing import Type


class ConvertCurrencyTool(BaseTool):
    name: str = "convert_currency"
    description: str = "Конвертирует сумму из одной валюты в другую по текущему курсу."
    args_schema: Type[BaseModel] = ConvertCurrencyArgs

    client: httpx.Client = Field(exclude=True)

    def _run(self, amount: float, from_currency: str,  to_currency: str) -> float | str:
        """
        Конвертирует заданную сумму из одной валюты в другую по актуальному курсу.
        """
        print("convert_currency")
        try:
            response = self.client.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
        except (httpx.ConnectTimeout, httpx.ConnectError):
            return "Ошибка соединения с сервисом"

        rate = response.json()["rates"][to_currency]
        result = amount * rate
        return round(result, 2)

client = httpx.Client(timeout=1)
convert_currency_tool = ConvertCurrencyTool(client=client)


@tool
def iphone_price() -> float:
    """
    Возвращает стоимость одного iPhone в рублях.
    """
    print("iphone_price")
    return 85_000.


@tool
def current_time() -> str:
    """
    Возвращает текущую дату и время в формате %Y-%m-%d %H:%M:%S.
    """
    print("current_time")
    return dt.now().strftime("%Y-%m-%d %H:%M:%S")

