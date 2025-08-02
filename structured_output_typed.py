from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Annotated

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest')

class Review(BaseModel):
    summary: Annotated[str, "a small summary of 10 words"]
    sentiment: Annotated[str, "return a sentiment of the review in positive, negative, neutral"]

structured_model = model.with_structured_output(Review)

 
result = structured_model.invoke("""
    OpenAI is a leading force in AI, pushing boundaries with large language models, image generation, and a focus on safety.
""")


print(result)

