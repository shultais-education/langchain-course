from pathlib import Path


def get_books(books: list[tuple[str, Path]]):
    for book_name, book in books:
        yield book_name, book.read_text(encoding="utf-8")
