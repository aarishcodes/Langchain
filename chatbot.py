from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest')

memory = [
    SystemMessage(content="You are help full Assistent")
]
while True:
    user_input = input('You:')
    memory.append(HumanMessage(content=user_input))
    if(user_input == 'exit'):
        break;
    
    result = model.invoke(memory)
    memory.append(AIMessage(content=result.content))
    print("AI:", result.content)
print(memory)