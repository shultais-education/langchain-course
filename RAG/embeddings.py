from pathlib import Path
from RAG.splitter import get_chunks
from langchain_ollama import OllamaEmbeddings


chunks = get_chunks(Path("./docs/war-and-peace-1.txt"))
first_chunk = chunks[1]
embedder = OllamaEmbeddings(model="qwen3-embedding:0.6b", base_url="http://localhost:11434")
vector = embedder.embed_query(first_chunk.page_content)
print(vector)
print(len(vector))
