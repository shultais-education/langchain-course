import asyncio
import json
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from langchain_core.documents import Document
from RAG.services.loaders import get_books
from RAG.services.splitters import get_book_chunks
from RAG.services.vectorstore import vectorstore_q

rag_path = Path(__file__).parent.parent
books_path = rag_path / "docs"

books = [(book.stem, book) for book in books_path.glob("war-and-peace-*.txt")]


def save_chunks():
    chunks = []
    for book_name, book_text in get_books(books):
        book_chunks = get_book_chunks(book_text)

        for book_chunk in book_chunks:
            doc_id = hash((book_name, book_chunk.metadata.get("Часть"), book_chunk.metadata.get("Глава")))
            chunk_id = hash((doc_id, book_chunk.page_content[:100]))
            book_chunk.metadata.update({"Книга": book_name, "doc_id": doc_id, "chunk_id": chunk_id})

            chunks.append({
                "page_content": book_chunk.page_content,
                "metadata": book_chunk.metadata
            })

    with open(books_path / "chunks.json", "w") as f:
        json.dump(chunks, f, ensure_ascii=False)


def load_chunks():
    with open(books_path / "chunks.json", "r") as f:
        chunks = json.load(f)
        for i, chunk in enumerate(chunks):
            chunks[i] = Document(**chunk)
    return chunks


async def full_index():
    book_chunks = load_chunks()
    await vectorstore_q.aadd_documents(documents=book_chunks)


if __name__ == "__main__":
    asyncio.run(full_index())
