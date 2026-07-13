from langchain_docling.loader import DoclingLoader, ExportType

FILE_PATH = "../docs/techweek.pdf"

loader = DoclingLoader(file_path=FILE_PATH, export_type=ExportType.MARKDOWN)

documents = loader.load()

for document in documents:
    print(document.page_content)
    print(document)
    print("- " * 50)
