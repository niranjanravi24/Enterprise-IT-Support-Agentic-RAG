from app.services.ingestion import load_file, chunk_documents
from pathlib import Path
from app.rag.vectorstore import add_documents


docs = load_file(Path("data/sample_kb/company_it_handbook.md"))
chunks = chunk_documents(docs)

add_documents(chunks)
# from app.core.config import get_settings

# settings = get_settings()

# print("Embedding model:", settings.embedding_model)
# print("OpenAI model:", settings.openai_model)
# print("OpenAI key configured:", bool(settings.openai_api_key))