from vectorstore.embeddings import get_embedding_model

embedding_model = get_embedding_model()

vector = embedding_model.embed_query(
    "KeyError in Python dictionary"
)

print(len(vector))
print(vector[:10])