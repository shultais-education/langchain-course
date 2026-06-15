from dotenv import load_dotenv
load_dotenv()

from MenuAssistant.prompts import choice_prompt, chef_prompt
from MenuAssistant.models import choice_model, recipe_model
from MenuAssistant.parsers import sort_dishes, make_markdown

# Выбор блюда
text = input("Для чего предложить блюда: ")
dishes = (choice_prompt | choice_model | sort_dishes).invoke({"text": text})

for i, dish in enumerate(dishes):
    print(f"{i+1}. {dish}")

num = input("\nВыберите блюдо (1-5): ")
num = int(num.strip()) - 1

# Приготовление
recipe = (chef_prompt | recipe_model | make_markdown).invoke({"dish": dishes[num]})
print(recipe)
