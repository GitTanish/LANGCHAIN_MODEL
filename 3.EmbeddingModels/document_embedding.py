from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# embedding = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

embedding = HuggingFaceEmbeddings(
    model_name="nomic-ai/nomic-embed-text-v1",
    model_kwargs={"trust_remote_code": True}
)
document = [
    "The nomic-ai/nomic-embed-text-v1 model is what's called a Matryoshka (MRL) model. This means it's designed to have its embeddings truncated to smaller sizes without losing much quality.",
    "However, the HuggingFaceEmbeddings wrapper doesn't know this. It will always return the model's full, native embedding"
]
# so nomic here have better benchmark than text-embedding-3-small (they're almost equal)
result = embedding.embed_documents(document)
print(str(result))