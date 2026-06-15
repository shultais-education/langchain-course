from random import choice
from dotenv import load_dotenv
load_dotenv()

from MenuAssistant.chains import dishes_chain
from MenuAssistant.callbacks import BaseCallback

# Выбор блюда
text = input("Для чего предложить блюда: ")
dishes = dishes_chain.invoke({"text": text}, config={"callbacks": [BaseCallback()]})

# for i, dish in enumerate(dishes):
#     print(f"{i+1}. {dish}")

