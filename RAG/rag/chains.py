from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from RAG.rag.models import gemini_model, queries_generator_model
from RAG.rag.retriver import book_retriever
from RAG.rag.prompts import prompt, multi_query_prompt
from RAG.rag.parsers import format_docs, queries_list


queries_chain = RunnableParallel(
    queries=multi_query_prompt | queries_generator_model | RunnableLambda(lambda a: a.queries),
    book=RunnableLambda(lambda q: q["book"])
) | queries_list


rag_chain = (
    RunnableParallel(
        queries=queries_chain,
        question=RunnableLambda(lambda q: q["question"]),
        book=RunnableLambda(lambda q: q["question"])
    )
    |
    RunnableParallel({
        "context": RunnableLambda(lambda x: x["queries"]) | book_retriever.map() | format_docs,
        "question": RunnableLambda(lambda q: q["question"]),
        "book": RunnableLambda(lambda q: q["book"])
    })
    | prompt
    | gemini_model
    | StrOutputParser()
)
