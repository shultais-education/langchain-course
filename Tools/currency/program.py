from dotenv import load_dotenv
load_dotenv()

from Tools.currency.tools import convert_currency_tool, iphone_price, current_time
from RAG.tools import rag
from Tools.currency.prompts import currency_prompt, tools_prompt
from Tools.currency.models import gpt_model
from Tools.currency.schemas import ToolAnswer, AgentContext, StateSchema
from langchain.agents import create_agent
from langchain.agents.structured_output import ProviderStrategy
from langchain.agents.middleware import ToolRetryMiddleware, PIIMiddleware
from Tools.currency.middleware import (before_agent_middleware, after_agent_middleware,
                                       before_model_middleware, after_model_middleware)


text = input("Что конвертируем? ")


tools = [convert_currency_tool, iphone_price, rag, current_time]
tools_agent = create_agent(
    model=gpt_model,
    tools=tools,
    system_prompt=tools_prompt,
    context_schema=AgentContext,
    state_schema=StateSchema,
    response_format=ProviderStrategy(ToolAnswer),
    middleware=[ToolRetryMiddleware(
        tools=["current_time"],
        max_retries=3,
        initial_delay=0,
        retry_on=(ValueError,)
    ), PIIMiddleware("email", strategy="mask"),
        before_agent_middleware,
        after_agent_middleware,
        before_model_middleware,
        after_model_middleware]
)

result = tools_agent.invoke(
    input={
        "messages": currency_prompt.invoke({"text": text}),
        "models_calls": 0
    },
    context=AgentContext(user_id=10, db={"connection_id": 20})
)

if "structured_response" in result:
    print(result["structured_response"].answer)
    print(result["structured_response"].answer_date)
else:
    print(result["messages"][-1].text)
