from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
    Ответь на вопрос, используя контекст ниже.
    Если ответа в контексте нет, так и скажи.
    
    Контекст: {context}
    
    Вопрос: {question}
    
    Ответ: 
""")
