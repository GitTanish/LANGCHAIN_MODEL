from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="nomic-ai/nomic-embed-text-v1",
    model_kwargs={"trust_remote_code": True}
)

documents = [
    
    "The nomic-ai/nomic-embed-text-v1 model is what's called a Matryoshka (MRL) model. This means it's designed to have its embeddings truncated to smaller sizes without losing much quality.",
    "However, the HuggingFaceEmbeddings wrapper in LangChain doesn't know this. It will always return the model's full, native embedding, so you must slice it manually.",
    "According to the MTEB benchmark, nomic-embed-text-v1 outperforms OpenAI's text-embedding-3-small and the older text-embedding-ada-002.",
    "This Nomic model is very efficient, taking up only about 500MB of RAM, making it ideal for systems with 8GB of memory or less.",
    "A popular high-performance alternative is BAAI/bge-large-en-v1.5, which offers top-tier accuracy but requires a powerful GPU and much more VRAM.",
    #Added - Irrelevant
    "The best way to cook a steak is by searing it on a hot cast-iron skillet with butter, garlic, and thyme."
]

query = "What is a good model for a computer with low RAM?"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

print(cosine_similarity([query_embedding],doc_embeddings))
scores = cosine_similarity([query_embedding],doc_embeddings)
# [[0.55086155 0.36318863 0.44482262 0.68624298 0.47083656 0.28191916]]
# looks great since, 0.68 is the score, the query is correctly retrieving from 4th doc 
index, score = sorted(list(enumerate(scores)), key = lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)

# --- DEBUGGING STARTS HERE ---

print("\nCalculating similarities...")
scores = cosine_similarity([query_embedding], doc_embeddings)
print("Raw scores:", scores) # DEBUG 1: Check raw scores

score_list = scores[0]
indexed_scores = list(enumerate(score_list))
print("Indexed scores (before sorting):", indexed_scores) # DEBUG 2: Check pairs

sorted_indexed_scores = sorted(indexed_scores, key = lambda x:x[1])
print("Sorted indexed scores:", sorted_indexed_scores) # DEBUG 3: Check the full sorted list

index, score = sorted_indexed_scores[-1]
print(f"Highest score found: Index={index}, Score={score}") # DEBUG 4: Check extracted index and score

# --- DEBUGGING ENDS HERE ---

print("\n--- Final Result ---")
print("Query:", query)
print("Retrieved Document (Index {}):".format(index), documents[index])
print("Similarity score:", score)