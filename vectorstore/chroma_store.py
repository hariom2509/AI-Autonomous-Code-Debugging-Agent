from langchain_chroma import Chroma
from vectorstore.embeddings import get_embedding_model


def get_vector_store():

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        collection_name="codebase",
        embedding_function=embedding_model,
        persist_directory="./chroma_db"
    )

    return vector_store