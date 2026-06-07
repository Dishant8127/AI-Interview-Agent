from pinecone import Pinecone

from langchain_pinecone import PineconeVectorStore

from config.settings import (
    PINECONE_API_KEY,
    PINECONE_INDEX
)

from rag.embeddings import get_embeddings


def clear_index():

    pc = Pinecone(
        api_key=PINECONE_API_KEY
    )

    index = pc.Index(
        PINECONE_INDEX
    )

    index.delete(
        delete_all=True
    )


def create_vector_store(chunks):

    pc = Pinecone(
        api_key=PINECONE_API_KEY
    )

    index = pc.Index(
        PINECONE_INDEX
    )

    vector_store = PineconeVectorStore(
        index=index,
        embedding=get_embeddings()
    )

    vector_store.add_documents(
        chunks
    )

    return vector_store