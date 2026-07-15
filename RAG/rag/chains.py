from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from RAG.rag.models import gemini_model
from RAG.rag.retriver import book_retriever
from RAG.rag.prompts import prompt
from RAG.rag.parsers import format_docs


rag_chain = (
    {
        "context": book_retriever | format_docs,
        "question": RunnableLambda(lambda q: q["question"])
    }
    | prompt
    | gemini_model
    | StrOutputParser()
)
