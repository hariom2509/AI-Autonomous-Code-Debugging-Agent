from vectorstore.chroma_store import get_vector_store


def retrieve_code(error_info, k=5):

    vector_store = get_vector_store()

    # Build search query from error info
    query = f"""
    error_type: {error_info.get("error_type") if isinstance(error_info, dict) else error_info}
    file: {error_info.get("file")}
    function: {error_info.get("function")}
    """

    docs = vector_store.similarity_search(query, k=k)

    code_chunks = []

    for doc in docs:
        code_chunks.append(doc.page_content)

    return code_chunks