from dotenv import load_dotenv
load_dotenv()

from Tools.currency.tools import convert_currency_tool, iphone_price
from RAG.tools import rag
from Tools.currency.prompts import currency_prompt, tools_prompt
from Tools.currency.models import gemini_model
from langchain.agents import create_agent


text = input("Что конвертируем? ")


tools = [convert_currency_tool, iphone_price, rag]
tools_agent = create_agent(model=gemini_model, tools=tools, system_prompt=tools_prompt)
result = tools_agent.invoke({"messages": currency_prompt.invoke({"text": text})})
print(result["messages"][-1].text)
