from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from schemas.translates import TranslatedText
load_dotenv()

default_tone = "дружелюбный"
base_template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template_file("prompts/system.txt", input_variables=["lang"]),
    SystemMessagePromptTemplate.from_template("Твой стиль общения: {tone}"),
    HumanMessagePromptTemplate.from_template("Скажи '{text}' на трех языках")
])
template = base_template.partial(lang="славянским", tone=default_tone)

text = input("Введите текст: ")
prompt = template.format_messages(text=text)

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=1, timeout=120, max_retries=0)
structured_model = model.with_structured_output(TranslatedText, strict=True)

response = structured_model.invoke(prompt)

# Pydantic модель
for translate in response.translates:
    print(f"{translate.language: >12}: {translate.text}")


# Словарь
# print(response.model_dump())
