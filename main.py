from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv()


model = ChatOpenAI(model="gpt-5.4-pro", temperature=1, timeout=(10, 120), max_retries=0)
response = model.invoke([
    SystemMessage(content="Ты специалист по славянским языкам."),
    HumanMessage(content="Скажи 'Привет' на трех языках"),
])


print(response.content)
