from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import get_settings

settings = get_settings()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=settings.openai_api_key,
    timeout=30,
    max_retries=1,
)

response = model.invoke("Reply with: Gemini is working!")

print(response.content)