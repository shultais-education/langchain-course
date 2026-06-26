from Storm.prompts import asian_recipe_prompt, german_recipe_prompt, russian_recipe_prompt, french_recipe_prompt
from Storm.models import recipe_model
from Storm.parsers import make_markdown, compile_recipe
from langchain_core.runnables import RunnableParallel


def recipe_chain(cuisine_prompt):
    return cuisine_prompt | recipe_model | make_markdown


asian_recipe_chain = recipe_chain(asian_recipe_prompt)
german_recipe_chain = recipe_chain(german_recipe_prompt)
russian_recipe_chain = recipe_chain(russian_recipe_prompt)
french_recipe_chain = recipe_chain(french_recipe_prompt)

recipes_chain = RunnableParallel({
    "asian": asian_recipe_chain,
    "german": german_recipe_chain,
    "russian": russian_recipe_chain,
    "french": french_recipe_chain,
}) | compile_recipe
