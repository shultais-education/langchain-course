from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

game_template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template_file("prompts/game.txt", input_variables=[])
])

human_prompt = HumanMessagePromptTemplate.from_template("{text}")
