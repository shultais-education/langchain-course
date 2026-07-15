from dotenv import load_dotenv
load_dotenv()

from RAG.chains import rag_chain

question = "Сколько лет было графине"
answer = rag_chain.invoke(question)
print(answer)
