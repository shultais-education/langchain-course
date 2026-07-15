from dotenv import load_dotenv
load_dotenv()

from RAG.rag.chains import rag_chain

question = "Кто сказал фразу: Рана не здесь, а вот где"
answer = rag_chain.invoke({"question": question, "book": None})
print(answer)
