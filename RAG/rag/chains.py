from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from RAG.rag.models import gemini_model
from RAG.rag.retriver import retriever
from RAG.rag.prompts import prompt
from RAG.rag.parsers import format_docs


rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | gemini_model
    | StrOutputParser()
)
