from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from MenuAssistant.schemas import GeneratedMenu, GeneratedRecipe
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError

load_dotenv()

# Модели
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0, timeout=120, max_retries=0)
gpt_model = ChatOpenAI(model="gpt-4.1-mini", temperature=0, timeout=120, max_retries=0)

# Структурированные модели
choice_model = gemini_model.with_structured_output(GeneratedMenu, strict=True)
recipe_model = gemini_model.with_structured_output(GeneratedRecipe, strict=True)

choice_model_fallback = gpt_model.with_structured_output(GeneratedMenu, strict=True)
recipe_model_fallback = gpt_model.with_structured_output(GeneratedRecipe, strict=True)

choice_model = choice_model.with_fallbacks(
    fallbacks=[choice_model_fallback],
    exceptions_to_handle=(ChatGoogleGenerativeAIError,),
)
