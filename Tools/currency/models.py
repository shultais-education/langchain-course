from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from Tools.currency.tools import convert_currency

# Модели
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0, timeout=120, max_retries=0)
gpt_model = ChatOpenAI(model="gpt-4.1-mini", temperature=0, timeout=120, max_retries=0)

currency_model = gemini_model.bind_tools([convert_currency])
