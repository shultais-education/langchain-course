from RAG.rag.chains import rag_chain
from langchain_core.tools import tool


@tool("common_question", description="Общие вопросы пользователя", return_direct=True)
def rag(question: str) -> str:
    print("rag")
    return rag_chain.invoke({"question": question, "book": None})
