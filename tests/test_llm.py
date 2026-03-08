from config.llm import get_llm

llm = get_llm()

response = llm.invoke(
    "Explain KeyError in Python in 2 lines."
)

print(response.content)