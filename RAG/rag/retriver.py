from RAG.services.vectorstore import vectorstore_q
from langchain_core.runnables import RunnableLambda
from RAG.services.indexer import load_chunks
from langchain_community.retrievers import BM25Retriever


base_retriever = vectorstore_q.as_retriever(search_type="mmr", search_kwargs={"k": 6, "fetch_k": 24, "lambda_mult": 0.4})


def book_retriever_func(question: dict):
    search_params = {"k": 6, "fetch_k": 24, "lambda_mult": 0.4}

    book = question.get("book")
    question = question["question"]

    if book:
        search_params["filter"] = {
            "must": [{"key": "metadata.Книга","match": {"value": book}}]
        }

    return vectorstore_q.\
        as_retriever(search_type="mmr", search_kwargs=search_params).\
        invoke(question)

book_retriever = RunnableLambda(book_retriever_func)


def book_bm25_retriever_func(question: dict):
    chunks = load_chunks()
    retriever = BM25Retriever.from_documents(chunks, k=5)

    book = question.get("book")
    question = question["question"]

    results = []
    for doc in retriever.invoke(question):
        if book and doc.metadata.get("book") != book:
            continue
        results.append(doc)

    return results

book_bm25_retriever = RunnableLambda(book_bm25_retriever_func)
