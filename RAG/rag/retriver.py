from RAG.services.vectorstore import vectorstore_q
from langchain_core.runnables import RunnableLambda

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
