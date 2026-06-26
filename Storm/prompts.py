from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnableLambda


chef_template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template("Ты повар {cuisine} кухни."),
    HumanMessagePromptTemplate.from_template("Предложи вариацию рецепта: {dish}")
])

asian_chef_template = chef_template.partial(cuisine="азиатской")
french_chef_template = chef_template.partial(cuisine="французской")
russian_chef_template = chef_template.partial(cuisine="русской")
german_chef_template = chef_template.partial(cuisine="немецкой")


asian_recipe_prompt = RunnableLambda(lambda i: asian_chef_template.format_messages(dish=i["dish"]))
french_recipe_prompt = RunnableLambda(lambda i: french_chef_template.format_messages(dish=i["dish"]))
russian_recipe_prompt = RunnableLambda(lambda i: russian_chef_template.format_messages(dish=i["dish"]))
german_recipe_prompt = RunnableLambda(lambda i: german_chef_template.format_messages(dish=i["dish"]))
