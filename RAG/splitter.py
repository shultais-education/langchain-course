from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import MarkdownHeaderTextSplitter

def get_chunks(file: Path):

    with open(file) as f:
        text = f.read()

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

    book_chunks = book_splitter.split_text(text)
    chunks = text_splitter.split_documents(book_chunks)

    return chunks
