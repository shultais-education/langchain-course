from dotenv import load_dotenv
load_dotenv()

from Storm.chains import recipes_chain


# Выбор блюда
dish = input("Какое блюдо готовим: ")
recipes = recipes_chain.invoke({"dish": dish})

print(recipes)
