from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from prompts.game import game_template

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=1, timeout=120, max_retries=0)
history = InMemoryChatMessageHistory()

while True:
    text = input("🙋‍♂️Сообщение: ")

    if text == "":
        break

    human_message = HumanMessage(content=text)
    messages = game_template.format_messages() + history.messages + [human_message]
    response = model.invoke(messages)

    print("🤖Бот:", response.text)

    history.add_message(human_message)
    history.add_message(AIMessage(content=response.content))

    if "угадал" in text.lower():
        history.clear()
