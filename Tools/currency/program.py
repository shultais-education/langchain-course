from dotenv import load_dotenv
load_dotenv()

from Tools.currency.chains import currency_chain
from Tools.currency.tools import convert_currency, iphone_price
from Tools.currency.prompts import currency_prompt_template
from Tools.currency.models import currency_model
from langchain_core.messages import ToolMessage


text = input("Что конвертируем? ")
result = currency_chain.invoke({"text": text})
# print(result)

tools = {
    "convert_currency": convert_currency,
    "iphone_price": iphone_price,
}

tool_messages = []

tool_calls = result.tool_calls
if tool_calls:
    for tool_call in tool_calls:
        tool = tools[tool_call["name"]]
        output = tool.invoke(tool_call["args"])
        tool_messages.append(
            ToolMessage(tool_call_id=tool_call["id"], content=output)
        )

    messages = currency_prompt_template.format_messages(text=text)
    messages += [result]
    messages += tool_messages

    final_result = currency_model.invoke(messages)
    print(final_result.text)

else:
    print(result.text)
