from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b', temperature=0.9, max_tokens=1000)

messages = [
    {"role": "system", "content": "You are an assistant, who's very consistent and precise."},
    {"role": "user", "content": "15 reasons of WHY TO USE LINUX, SINCE WINDOWS 10 WILL NOT RECIEVE ANY UPDATES"}
]

result = model.invoke(messages)
# Note: the usage pattern is the same for other providers — only the import and model class change.
# Examples (replace the import/class with the library you actually use):

# OpenAI example (pseudo-code — adapt to the OpenAI wrapper you use):
# from openai_library import ChatOpenAI
# openai_model = ChatOpenAI(model='gpt-4', temperature=0.9, max_tokens=1000)
# openai_result = openai_model.invoke(messages)  # or openai_model(messages) depending on the lib
# print(openai_result.content)

# Claude example (pseudo-code):
# from claude_library import ChatClaude
# claude_model = ChatClaude(model='claude-2', temperature=0.9, max_tokens=1000)
# claude_result = claude_model.invoke(messages)
# print(claude_result.content)

# Summary: keep `messages` and the call/response handling the same; swap only the import and model class.
# benefits of langchain
