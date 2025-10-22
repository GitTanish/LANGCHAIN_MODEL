from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# embedding = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

embedding = HuggingFaceEmbeddings(
    model_name="nomic-ai/nomic-embed-text-v1",
    model_kwargs={"trust_remote_code": True}
)
# so free models doesn't support dimensions parameter directly but it can be obtained through slicing
# I'm not using bge-large here cause it won't be feasible to run a large embedding model on ram
result =embedding.embed_query("Wubba Lubba Dub Dub")
print(str(result))