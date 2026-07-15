from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import MarkdownHeaderTextSplitter

book_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("##", "Часть"),
        ("###", "Глава"),
    ]
)

chunk_size = 1000
chunk_overlap = 150

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)


async def get_book_chunks(book_text: str):
    book_chunks = book_splitter.split_text(book_text)
    return text_splitter.split_documents(book_chunks)
