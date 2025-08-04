from langchain.schema.runnable import RunnableLambda

def word_counter(text):
    return len(text.split())

word_counter = RunnableLambda(word_counter)

result = word_counter.invoke("Hi Aarish, How is you Langchain Journey going on")

print(result)