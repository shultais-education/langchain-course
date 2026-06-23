from dotenv import load_dotenv
load_dotenv()

from Tools.currency.chains import currency_chain
from Tools.currency.tools import convert_currency

text = input("Что конвертируем? ")
tool_call = currency_chain.invoke({"text": text})

if tool_call:
    output = convert_currency.invoke(tool_call["args"])
    print(output)
