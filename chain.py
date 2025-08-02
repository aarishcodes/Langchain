from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest', max_tokens= 10)

prompt = PromptTemplate(
    template='Genereate 5 interesting facts about {topic} in single line each',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    'topic': 'Bollywood'
})


print(result)


# chain.get_graph().print_ascii()