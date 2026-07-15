from dotenv import load_dotenv
load_dotenv()

from RAG.rag.chains import rag_chain

question = "Опиши внешний вид Болконского"
answer = rag_chain.invoke(question)
print(answer)
