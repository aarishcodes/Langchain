from langchain_community.tools import tool


@tool
def multiply(a: int, b: int) -> int:
    """This will multiply two numbers"""
    return a*b;


@tool
def divide(a: int, b: int) -> int:
    """this will divide two numbers"""
    return a/b;

result = divide.invoke({"a": 2, "b": 2}) 
print(result)

print(divide.name)
print(divide.description)
print(divide.args)


