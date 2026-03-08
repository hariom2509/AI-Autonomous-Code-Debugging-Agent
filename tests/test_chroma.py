from vectorstore.chroma_store import get_vector_store

vector_store = get_vector_store()

texts = [
    "user = request.data['user_id']",
    "user = request.data.get('user_id')",
    "print('Hello world')"
]

vector_store.add_texts(texts)

results = vector_store.similarity_search(
    "KeyError user_id",
    k=2
)

for r in results:
    print(r.page_content)