from vectorstore.chroma_store import get_vector_store


def search_code(query, k=5):

    vector_store = get_vector_store()

    docs = vector_store.similarity_search(query, k=k)

    results = []

    for doc in docs:

        results.append(doc.page_content)

    return results

# query
#   ↓
# embedding created
#   ↓
# ChromaDB similarity search
#   ↓
# return most relevant code chunks