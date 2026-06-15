from dotenv import load_dotenv
load_dotenv()

from MenuAssistant.chains import dishes_chain, recipe_chain

# Выбор блюда
text = input("Для чего предложить блюда: ")
dishes = dishes_chain.invoke({"text": text})

for i, dish in enumerate(dishes):
    print(f"{i+1}. {dish}")

num = input("\nВыберите блюдо (1-5): ")
num = int(num.strip()) - 1

# Приготовление
recipe = recipe_chain.invoke({"dish": dishes[num]})
print(recipe)
