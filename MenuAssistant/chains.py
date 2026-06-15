from MenuAssistant.prompts import choice_prompt, chef_prompt
from MenuAssistant.models import choice_model, recipe_model
from MenuAssistant.parsers import sort_dishes, make_markdown


dishes_chain = choice_prompt | choice_model | sort_dishes
recipe_chain = chef_prompt | recipe_model | make_markdown
