from random import choice

from MenuAssistant.schemas import GeneratedMenu, GeneratedRecipe
from langchain_core.runnables import RunnableLambda


def sort_dishes_func(menu: GeneratedMenu):
    raise ValueError("Ошибка сортировки")
    return sorted(menu.dishes)

sort_dishes = RunnableLambda(sort_dishes_func)


def make_markdown_func(recipe: GeneratedRecipe):
    md = f"# Готовим {recipe.name}\n"
    md += f"\n## Ингредиенты\n"

    for i, ingredient in enumerate(recipe.ingredients, start=1):
        md += f"{i}. {ingredient}\n"

    md += f"\n## Рецепт\n"
    for i, step in enumerate(recipe.steps, start=1):
        md += f"{i}. {step}\n"

    return md

make_markdown = RunnableLambda(make_markdown_func)

random_dish = RunnableLambda(lambda dishes: choice(dishes))
dish_to_dict = RunnableLambda(lambda dish_str: {"dish": dish_str})
