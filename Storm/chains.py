from Storm.prompts import asia_recipe_prompt, germany_recipe_prompt, russian_recipe_prompt, french_recipe_prompt
from Storm.models import recipe_model
from Storm.parsers import make_markdown


def recipe_chain(cuisine_prompt):
    return cuisine_prompt | recipe_model | make_markdown


asia_recipe_chain = recipe_chain(asia_recipe_prompt)
germany_recipe_chain = recipe_chain(germany_recipe_prompt)
russian_recipe_chain = recipe_chain(russian_recipe_prompt)
french_recipe_chain = recipe_chain(french_recipe_prompt)
