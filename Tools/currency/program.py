from dotenv import load_dotenv
load_dotenv()

from Tools.currency.chains import currency_chain
from Tools.currency.tools import convert_currency

text = input("Что конвертируем? ")
result = currency_chain.invoke({"text": text})
print(result)

tool_calls = result.tool_calls
if tool_calls:
    for tool_call in tool_calls:
        if tool_call["name"] == "convert_currency":
            output = convert_currency.invoke(tool_call["args"])
            print(output)
else:
    print(result.text)
