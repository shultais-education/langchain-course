from dotenv import load_dotenv
load_dotenv()

from Storm.chains import asian_recipe_chain, french_recipe_chain, german_recipe_chain, russian_recipe_chain


# Выбор блюда
dish = input("Какое блюдо готовим: ")
recipe = asian_recipe_chain.invoke({"dish": dish})

print(recipe)

