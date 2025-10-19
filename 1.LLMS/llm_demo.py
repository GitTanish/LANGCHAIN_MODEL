from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-120b')

result=llm.invoke("What is the captial of India", )
# llms are old, chatmodel is a way to go
print(result)