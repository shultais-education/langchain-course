from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from MenuAssistant.schemas import GeneratedMenu, GeneratedRecipe

load_dotenv()

# Модели
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0, timeout=120, max_retries=0)
gpt_model = ChatOpenAI(model="gpt-4.1-mini", temperature=0, timeout=120, max_retries=0)

# Структурированные модели
choice_model = gemini_model.with_structured_output(GeneratedMenu, strict=True)
recipe_model = gpt_model.with_structured_output(GeneratedRecipe, strict=True)
