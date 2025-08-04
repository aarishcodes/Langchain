from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.output_parsers import StrOutputParser



load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest', max_tokens=10)

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal['Positive', 'Negative'] = Field(description="Give the sentiment of the feedback")


parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='classifiy the following feedback in positive and negative of the following \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Generate me a Positive response for the feedback \n {feedback}",
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template="Generate me a Negative response for the feedback \n {feedback}",
    input_variables=['feedback']
)

classifier = prompt1 | model | parser2 


branch = RunnableBranch(
    (lambda x: x.sentiment == 'Positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'Negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not found a sentiment")
)

chain = classifier | branch

result = chain.invoke({
    'feedback': 'this is a teriable phone'
})


print(result)
 


