from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


model = ChatOpenAI(model="gpt-4.1-mini")
response = model.invoke("Скажи 'Привет'")
print(response.content)
