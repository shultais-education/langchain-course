from langchain_unstructured import UnstructuredLoader

file_paths = [
    "../docs/techweek.pdf",
]

loader = UnstructuredLoader(file_path=file_paths)
docs = loader.load()

for doc in docs:
    print(doc)
    print("- " * 50)
