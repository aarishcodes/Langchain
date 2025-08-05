from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
import math

def generate_numbers(n):
    return [i for i in range(1, n + 1)]

def compute_square_roots(numbers):
    return [math.sqrt(i) for i in numbers]

def format_results(numbers, roots):
    formatted = []
    for num, root in zip(numbers, roots):
        formatted.append(f"√{num} = {root:.2f}")
    return formatted

def main():
    numbers = generate_numbers(10)
    roots = compute_square_roots(numbers)
    results = format_results(numbers, roots)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()

"""

spliter = RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

result = spliter.split_text(text)
print(result)