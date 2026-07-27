from dotenv import load_dotenv
load_dotenv()

from Tools.currency.tools import convert_currency_tool, iphone_price, current_time
from RAG.tools import rag
from Tools.currency.prompts import currency_prompt, tools_prompt
from Tools.currency.models import gemini_model, gpt_model
from Tools.currency.schemas import ToolAnswer
from langchain.agents import create_agent
from langchain.agents.structured_output import ProviderStrategy, ToolStrategy


text = input("Что конвертируем? ")


tools = [convert_currency_tool, iphone_price, rag, current_time]
tools_agent = create_agent(model=gpt_model, tools=tools, system_prompt=tools_prompt,
                           response_format=ProviderStrategy(ToolAnswer))
result = tools_agent.invoke({"messages": currency_prompt.invoke({"text": text})})

if "structured_response" in result:
    print(result["structured_response"].answer)
    print(result["structured_response"].answer_date)
else:
    print(result["messages"][-1].text)
