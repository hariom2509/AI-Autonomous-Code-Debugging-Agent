from langchain_ollama import ChatOllama


def get_llm():

    llm = ChatOllama(
        model="deepseek-coder:6.7b",
        temperature=0
    )

    return llm