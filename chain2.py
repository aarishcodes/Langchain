from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest')

prompt1 = PromptTemplate(
    template='Give me a detailed Summery on Hollywood on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Extract 2 important points from the {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({
    'topic': 'actors'
})


print(result)