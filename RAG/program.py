from dotenv import load_dotenv
load_dotenv()

from RAG.rag.chains import rag_chain

question = "Опиши внешний вид жены Болконского"
answer = rag_chain.invoke({"question": question, "book": "war-and-peace-2"})
print(answer)
