from Storm.prompts import asian_recipe_prompt, german_recipe_prompt, russian_recipe_prompt, french_recipe_prompt
from Storm.models import recipe_model
from Storm.parsers import make_markdown


def recipe_chain(cuisine_prompt):
    return cuisine_prompt | recipe_model | make_markdown


asian_recipe_chain = recipe_chain(asian_recipe_prompt)
german_recipe_chain = recipe_chain(german_recipe_prompt)
russian_recipe_chain = recipe_chain(russian_recipe_prompt)
french_recipe_chain = recipe_chain(french_recipe_prompt)
