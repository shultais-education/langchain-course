from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from MenuAssistant.prompts import choice_template, chef_template
from MenuAssistant.schemas import GeneratedMenu, GeneratedRecipe

load_dotenv()

# Модели
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0, timeout=120, max_retries=0)
choice_model = gemini_model.with_structured_output(GeneratedMenu, strict=True)

gpt_model = ChatOpenAI(model="gpt-4.1-mini", temperature=0, timeout=120, max_retries=0)
recipe_model = gpt_model.with_structured_output(GeneratedRecipe, strict=True)

# Выбор блюда
text = input("Для чего предложить блюда: ")
choice_template = choice_template.partial(num=5)
choice_prompt = choice_template.format_messages(text=text)
choice_response = choice_model.invoke(choice_prompt)

for i, dish in enumerate(choice_response.dishes):
    print(f"{i+1}. {dish}")

num = input("\nВыберите блюдо (1-5): ")
num = int(num.strip()) - 1

# Приготовление
chef_prompt = chef_template.format_messages(dish=choice_response.dishes[num])
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
