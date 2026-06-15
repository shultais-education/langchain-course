from MenuAssistant.prompts import choice_prompt, chef_prompt
from MenuAssistant.models import choice_model, recipe_model
from MenuAssistant.parsers import sort_dishes, make_markdown, random_dish, dish_to_dict


dishes_chain = choice_prompt | choice_model | sort_dishes
recipe_chain = chef_prompt | recipe_model | make_markdown

super_chain = dishes_chain | random_dish | dish_to_dict | recipe_chain
