from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
st.header('Creative Writing Assistant')

topic_input = st.text_input("Enter your writing topic (e.g., A journey to a hidden city, The last star in the universe)", "")

tone_input = st.selectbox(
    "Select the tone of the writing",
    ["Formal", "Humorous", "Mysterious", "Dramatic", "Poetic"]
)

length_input = st.selectbox(
    "Select the length of the response",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed story)"]
)

template_text = """
You are a creative writing assistant.
Your task is to write a story based on the user's request.

Topic: {topic_input}
Tone: {tone_input}
Length: {length_input}

Please generate a compelling and well-structured piece of writing that fits these parameters.
"""

prompt = PromptTemplate(
    input_variables=["topic_input", "tone_input", "length_input"],
    template=template_text
)

if st.button('Generate Story'):
    if topic_input:
        chain = prompt | model
        
        result = chain.invoke({
            'topic_input': topic_input,
            'tone_input': tone_input,
            'length_input': length_input
        })

        st.write("### Your Generated Story:")
        st.write(result.content)
    else:
        st.warning("Please enter a writing topic to generate a story.")
