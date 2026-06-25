from dotenv import load_dotenv
load_dotenv()

from Storm.chains import asia_recipe_chain, french_recipe_chain, germany_recipe_chain, russian_recipe_chain


# Выбор блюда
dish = input("Какое блюдо готовим: ")
recipe = asia_recipe_chain.invoke({"dish": dish})

print(recipe)

