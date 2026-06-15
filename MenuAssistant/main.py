from random import choice
from dotenv import load_dotenv
load_dotenv()

from MenuAssistant.chains import dishes_chain, recipe_chain

# Выбор блюда
text = input("Для чего предложить блюда: ")
dishes = dishes_chain.invoke({"text": text})

# for i, dish in enumerate(dishes):
#     print(f"{i+1}. {dish}")

# Приготовление
recipes = recipe_chain.batch([{"dish": d, "price": 300} for d in dishes])
recipes = zip(dishes, recipes)
# [("название", "рецепт"), ("...", "...")]
for name, recipe in recipes:
    with open(f"recipes/{name}.md", "w") as f:
        f.write(recipe)
