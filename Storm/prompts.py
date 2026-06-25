from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnableLambda


chef_template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template("Ты повар {cuisine} кухни."),
    HumanMessagePromptTemplate.from_template("Предложи вариацию рецепта: {dish}")
])

asia_chef_template = chef_template.partial(cuisine="азиатской")
french_chef_template = chef_template.partial(cuisine="французской")
russian_chef_template = chef_template.partial(cuisine="русской")
germany_chef_template = chef_template.partial(cuisine="немецкой")


asia_recipe_prompt = RunnableLambda(lambda i: asia_chef_template.format_messages(dish=i["dish"]))
french_recipe_prompt = RunnableLambda(lambda i: french_chef_template.format_messages(dish=i["dish"]))
russian_recipe_prompt = RunnableLambda(lambda i: russian_chef_template.format_messages(dish=i["dish"]))
germany_recipe_prompt = RunnableLambda(lambda i: germany_chef_template.format_messages(dish=i["dish"]))
