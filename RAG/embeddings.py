from dotenv import load_dotenv
load_dotenv()

import asyncio
from pathlib import Path
from RAG.splitter import get_chunks
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client.models import Distance, VectorParams
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)
embedder = OllamaEmbeddings(model="qwen3-embedding:0.6b", base_url="http://localhost:11434")
vector_size = len(embedder.embed_query("пример текста"))

collection_name = "war-and-peace"
if not client.collection_exists(collection_name):
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )

vectorstore_q = QdrantVectorStore(client=client, collection_name=collection_name, embedding=embedder)


async def main():
    chunks = get_chunks(Path("./docs/war-and-peace-1.txt"))
    await vectorstore_q.aadd_documents(documents=chunks)

asyncio.run(main())
