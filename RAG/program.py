from dotenv import load_dotenv
load_dotenv()

from RAG.rag.chains import rag_chain

question = "Поясни за шмот Кутузова"
answer = rag_chain.invoke({"question": question, "book": None})
print(answer)
