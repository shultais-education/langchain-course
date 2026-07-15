from langchain_core.runnables import RunnableLambda


def format_docs_func(docs):
    return "\n\n".join(doc.page_content for doc in docs)

format_docs = RunnableLambda(format_docs_func)
