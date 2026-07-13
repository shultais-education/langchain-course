from langchain_unstructured import UnstructuredLoader
from unstructured.cleaners.core import clean_extra_whitespace


loader = UnstructuredLoader(
    web_url="https://shultais.education/blog/best-python-books-for-beginners",
    chunking_strategy="by_title",
    include_orig_elements=False,
    post_processors=[clean_extra_whitespace],
)
docs = loader.load()

for doc in docs:
    print(doc)
    print("- " * 50)
