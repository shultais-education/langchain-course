from langchain_google_genai import ChatGoogleGenerativeAI

gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0, timeout=120, max_retries=0)
