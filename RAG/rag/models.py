from langchain_google_genai import ChatGoogleGenerativeAI
from RAG.rag.schemas import MultiQueryOutput

gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0, timeout=120, max_retries=0)
queries_generator_model = gemini_model.with_structured_output(MultiQueryOutput, strict=True)
