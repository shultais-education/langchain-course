from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from Storm.schemas import GeneratedRecipe


load_dotenv()

# Модели
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0, timeout=120, max_retries=0)
gpt_model = ChatOpenAI(model="gpt-4.1-mini", temperature=0, timeout=120, max_retries=0)

# Структурированные модели
recipe_model = gemini_model.with_structured_output(GeneratedRecipe, strict=True)
