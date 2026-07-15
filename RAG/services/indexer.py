import asyncio
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from RAG.services.loaders import get_books
from RAG.services.splitters import get_book_chunks
from RAG.services.vectorstore import vectorstore_q

rag_path = Path(__file__).parent.parent
books_path = rag_path / "docs"

books = [(book.stem, book) for book in books_path.glob("war-and-peace-*.txt")]

async def full_index():
    for book_name, book_text in get_books(books):
        book_chunks = await get_book_chunks(book_text)

        for book_chunk in book_chunks:
            doc_id = hash((
                book_name,
                book_chunk.metadata.get("Часть"),
                book_chunk.metadata.get("Глава"))
            )
            book_chunk.metadata.update({"Книга": book_name, "doc_id": doc_id})

        await vectorstore_q.aadd_documents(documents=book_chunks)


asyncio.run(full_index())
