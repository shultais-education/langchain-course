from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("../docs/war-and-peace-1.txt") as f:
    text = f.read()

chunk_size = 1000
chunk_overlap = 150

text_splitter = RecursiveCharacterTextSplitter(
    separators=[r"\s#{2}\s.*\n", r"\s#{3}\s.*\n", "\n\n", "\n", " ", ""],
    is_separator_regex=True,
    chunk_size=chunk_size,
    keep_separator=False,
    chunk_overlap=chunk_overlap
)

chunks = text_splitter.split_text(text)
for chunk in chunks:
    print(chunk)
    print("- " * 50)
