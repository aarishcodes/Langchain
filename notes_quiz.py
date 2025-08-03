from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest')

prompt1= PromptTemplate(
    template="Generate a well structured Notes for the {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate me a 3 quiz Question from the {text}",
    input_variables=['text']
)

prompt3= PromptTemplate(
    template="Merge both of the response with the {notes} and {quiz}",
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model | parser,
    'quiz': prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

text = """
Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize food from carbon dioxide and water. 
Photosynthesis in plants generally involves the green pigment chlorophyll and generates oxygen as a byproduct.
"""
result = chain.invoke({
    'text': text
})



print(result)
