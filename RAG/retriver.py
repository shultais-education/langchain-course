from dotenv import load_dotenv

load_dotenv()

from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

collection_name = "war-and-peace"

client = QdrantClient(host="localhost", port=6333)
embedder = OllamaEmbeddings(model="qwen3-embedding:0.6b", base_url="http://localhost:11434")
vectorstore_q = QdrantVectorStore(client=client, collection_name=collection_name, embedding=embedder)


retriever = vectorstore_q.as_retriever(search_type="mmr", search_kwargs={"k": 6})
retriever_documents = retriever.invoke("Сколько лет было Графини")

for document in retriever_documents:
    print(document)
    print("- " * 50)
