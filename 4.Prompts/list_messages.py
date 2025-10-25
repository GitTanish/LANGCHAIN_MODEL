from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b', temperature=0.9, max_tokens=5000)

chat_history = [
    SystemMessage(content= "You are a very smart and composed AI assistant") # saves token :) 
]

while True:
    user_input= input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input =='bye':
        break
    result =  model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI:', result.content)
print(chat_history)

