from langchain_core.runnables import RunnableLambda


def document_source(document):
    metadata = document.metadata
    content = document.page_content
    source = "## Источник:\nТом: {}, Глава: {}, Часть: {}".format(
        metadata.get("Книга", "не указана"),
        metadata.get("Глава", "не указана"),
        metadata.get("Часть", "не указана")
    )
    context = f"## Контекст:\n{content}"
    return f"{source}\n{context}"

def format_docs_func(results):
    final_docs = {}

    # print(results)

    combined_results = [results["bm25_results"]]
    combined_results.extend(results["vector_results"])

    for result in combined_results:
        for rank, doc in enumerate(result):
            chunk_id = doc.metadata["chunk_id"]
            score = 1.0 / (rank + 1)
            if chunk_id not in final_docs:
                final_docs[chunk_id] = {"document": doc, "score": 0}
            final_docs[chunk_id]["score"] += score

    final_docs = sorted(final_docs.values(), key=lambda x: x["score"], reverse=True)[:12]
    return "\n\n".join(document_source(doc["document"]) for doc in final_docs)

format_docs = RunnableLambda(format_docs_func)


def queries_list_func(inputs: dict):
    return [{"question": i, "book": inputs["book"]} for i in inputs["queries"]]

queries_list = RunnableLambda(queries_list_func)
