from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from RAG.models import gemini_model
from RAG.retriver import retriever
from RAG.prompts import prompt
from RAG.parsers import format_docs


rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | gemini_model
    | StrOutputParser()
)
