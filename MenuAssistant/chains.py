from MenuAssistant.prompts import choice_prompt, chef_prompt
from MenuAssistant.models import choice_model, recipe_model, choice_model_fallback
from MenuAssistant.parsers import sort_dishes, make_markdown, random_dish, dish_to_dict
from langchain_core.runnables import RunnableLambda


def get_dishes_chain(llm):
    return choice_prompt | llm | sort_dishes


dishes_chain = get_dishes_chain(choice_model)
dishes_chain_fallback = get_dishes_chain(choice_model_fallback)
emergency_dishes_chain = RunnableLambda(lambda i: ["Хлеб с маслом"])

dishes_chain = dishes_chain.with_fallbacks(
    fallbacks=[emergency_dishes_chain],
    exceptions_to_handle=[ValueError],
)


recipe_chain = chef_prompt | recipe_model | make_markdown
super_chain = dishes_chain | random_dish | dish_to_dict | recipe_chain
