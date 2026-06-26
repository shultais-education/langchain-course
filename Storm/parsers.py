from Storm.schemas import GeneratedRecipe
from langchain_core.runnables import RunnableLambda


def make_markdown_func(recipe: GeneratedRecipe):
    md = f"## {recipe.name}\n"
    md += f"\n### Ингредиенты\n"

    for i, ingredient in enumerate(recipe.ingredients, start=1):
        md += f"{i}. {ingredient}\n"

    md += f"\n### Рецепт\n"
    for i, step in enumerate(recipe.steps, start=1):
        md += f"{i}. {step}\n"

    return md

make_markdown = RunnableLambda(make_markdown_func)
