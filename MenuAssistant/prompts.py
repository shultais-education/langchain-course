from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_core.runnables import RunnableLambda


choice_template = ChatPromptTemplate([
    SystemMessage(content="Ты ассистент по выбору блюд для готовки дома."),
    SystemMessagePromptTemplate.from_template("Твоя задача предложить {num} вариантов блюд. Только названия."),
    HumanMessagePromptTemplate.from_template("Составь список для: {text}")
])

choice_template = choice_template.partial(num=3)

def choice_prompt_func(input: dict):
    print("Генерация промпта")
    return choice_template.format_messages(text=input["text"])

choice_prompt = RunnableLambda(choice_prompt_func)


chef_template = ChatPromptTemplate([
    SystemMessage(content="Ты домашний повар, который умеет готовить вкусную и полезную еду из продуктов, доступных в магазине."),
    SystemMessage(content="Твоя задача предложить простой рецепт со списком ингредиентов и последовательными шагами."),
    HumanMessagePromptTemplate.from_template("Предложи рецепт для приготовления: {dish} до {price} рублей.")
])


chef_prompt = RunnableLambda(lambda i: chef_template.format_messages(dish=i["dish"], price=i["price"]))


