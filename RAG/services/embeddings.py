from langchain_ollama import OllamaEmbeddings

embedder = OllamaEmbeddings(model="qwen3-embedding:0.6b", base_url="http://localhost:11434")
vector_size = len(embedder.embed_query("пример текста"))
