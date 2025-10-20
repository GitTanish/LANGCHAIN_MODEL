from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from langchain_community.llms import HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from dotenv import load_dotenv

print("--- DEBUG: Script started. ---")
loaded = load_dotenv()
print(f"--- DEBUG: .env file loaded? {loaded} ---")

api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN") # Check for the CORRECT name
access_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN") # Check for the WRONG name

if api_key:
    print(f"--- DEBUG: SUCCESS! Found HUGGINGFACEHUB_API_TOKEN. ---")
else:
    print("--- DEBUG: FAILED! HUGGINGFACEHUB_API_TOKEN was NOT found. ---")

if access_key:
    print(f"--- DEBUG: WARNING! Found old HUGGINGFACEHUB_ACCESS_TOKEN. ---")
# --- END DEBUG ---

llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.1",
    task="text-generation"
)
model= ChatHuggingFace(llm=llm)

result = model.invoke("Instructions to attain enlightenment")
print(result.content)
