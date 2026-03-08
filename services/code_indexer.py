import os
from tools.file_tools import get_python_files
from vectorstore.chroma_store import get_vector_store

def chunk_code(code, chunk_size=500):

    chunks = []

    for i in range(0, len(code), chunk_size):

        chunk = code[i:i + chunk_size]

        chunks.append(chunk)

    return chunks


def get_python_files(repo_path):

    python_files = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):

                python_files.append(
                    os.path.join(root, file)
                )

    return python_files



def index_repository(repo_path):

    vector_store = get_vector_store()

    files = get_python_files(repo_path)

    documents = []

    for file_path in files:

        with open(file_path, "r", encoding="utf-8") as f:

            code = f.read()

        chunks = chunk_code(code)

        documents.extend(chunks)

    vector_store.add_texts(documents)

    vector_store.persist()

    print("Repository indexed successfully")


# repo
#   ↓
# find python files
#   ↓
# read code
#   ↓
# split into chunks
#   ↓
# create embeddings
#   ↓
# store in ChromaDB