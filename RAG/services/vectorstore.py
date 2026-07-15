from dotenv import load_dotenv
load_dotenv()

from langchain_qdrant import QdrantVectorStore
from qdrant_client.models import Distance, VectorParams
from qdrant_client import QdrantClient
from RAG.services.embeddings import embedder, vector_size


client = QdrantClient(host="localhost", port=6333)

collection_name = "war-and-peace"
if not client.collection_exists(collection_name):
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )

vectorstore_q = QdrantVectorStore(client=client, collection_name=collection_name, embedding=embedder)
