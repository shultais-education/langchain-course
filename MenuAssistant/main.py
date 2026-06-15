from dotenv import load_dotenv
load_dotenv()

from MenuAssistant.prompts import chef_template, choice_prompt
from MenuAssistant.models import choice_model, recipe_model
from MenuAssistant.parsers import sort_dishes

# Выбор блюда
text = input("Для чего предложить блюда: ")
choice_response = choice_model.invoke(choice_prompt(text=text))
dishes = sort_dishes(choice_response)

for i, dish in enumerate(dishes):
    print(f"{i+1}. {dish}")

num = input("\nВыберите блюдо (1-5): ")
num = int(num.strip()) - 1

# Приготовление
chef_prompt = chef_template.format_messages(dish=dishes[num])
recipe_response = recipe_model.invoke(chef_prompt)

print(f"\n# Готовим {recipe_response.name}")
print()
print(f"## Ингредиенты\n")

for i, ingredient in enumerate(recipe_response.ingredients, start=1):
    print(f"{i}. {ingredient}")

print()
print(f"## Рецепт\n")
for i, step in enumerate(recipe_response.steps, start=1):
    print(f"{i}. {step}")
