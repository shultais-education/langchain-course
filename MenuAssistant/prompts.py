from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage


choice_template = ChatPromptTemplate([
    SystemMessage(content="Ты ассистент по выбору блюд для готовки дома."),
    SystemMessagePromptTemplate.from_template("Твоя задача предложить {num} вариантов блюд. Только названия."),
    HumanMessagePromptTemplate.from_template("Составь список для: {text}")
])


chef_template = ChatPromptTemplate([
    SystemMessage(content="Ты домашний повар, который умеет готовить вкусную и полезную еду из продуктов, доступных в магазине."),
    SystemMessage(content="Твоя задача предложить простой рецепт со списком ингредиентов и последовательными шагами."),
    HumanMessagePromptTemplate.from_template("Предложи рецепт для приготовления: {dish}")
])
