from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from openai import InternalServerError

from Tools.currency.tools import convert_currency, iphone_price

# Модели
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0, timeout=120, max_retries=0)
gpt_model = ChatOpenAI(model="gpt-4.1-mini", temperature=0, timeout=(10, 120), max_retries=0)

currency_model_fallback = gemini_model.bind_tools([convert_currency, iphone_price])
currency_model = gpt_model.with_fallbacks(
    fallbacks=[currency_model_fallback],
    exceptions_to_handle=(InternalServerError,)
).bind_tools([convert_currency, iphone_price])
