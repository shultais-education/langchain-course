from dotenv import load_dotenv
load_dotenv()

from RAG.rag.chains import rag_chain

question = "поясни за шмот жены Болконского"
answer = rag_chain.invoke({"question": question, "book": None})
print(answer)
