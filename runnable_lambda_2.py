from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableLambda, RunnableParallel, RunnableSequence, RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash-latest')

def word_counter(text):
    return len(text.split())


prompt = PromptTemplate(
    template="Give me a Joke on the {topic}",
    input_variables = ['topic']
)

parser = StrOutputParser()

gen_joke = RunnableSequence(prompt, model, parser)

final = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_counter)
})

final_chain = RunnableSequence(gen_joke, final)

result = final_chain.invoke({
    'topic': 'AI'
})

final_result ="""{} \n word Count - {}""".format(result['joke'], result['word_count'])


print(final_result)