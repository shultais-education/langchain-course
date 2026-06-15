from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.language_models.fake_chat_models import FakeListChatModel
from MenuAssistant.schemas import GeneratedMenu, GeneratedRecipe
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError
from openai import AuthenticationError

load_dotenv()

# Модели
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0, timeout=120, max_retries=0)
gpt_model = ChatOpenAI(model="gpt-4.1-mini", temperature=0, timeout=120, max_retries=0)
fake_model = FakeListChatModel(responses=["Творог"], sleep=0)

# Структурированные модели
choice_model = gemini_model.with_structured_output(GeneratedMenu, strict=True)
recipe_model = gemini_model.with_structured_output(GeneratedRecipe, strict=True)

choice_model_fallback = gpt_model.with_structured_output(GeneratedMenu, strict=True)
recipe_model_fallback = gpt_model.with_structured_output(GeneratedRecipe, strict=True)

choice_model_fallback = choice_model_fallback.with_fallbacks(
    fallbacks=[fake_model],
    exceptions_to_handle=(AuthenticationError,),
)

choice_model = choice_model.with_fallbacks(
    fallbacks=[choice_model_fallback],
    exceptions_to_handle=(ChatGoogleGenerativeAIError,),
)
