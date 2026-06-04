from pinecone import Pinecone

from langchain_pinecone import PineconeVectorStore

from config.settings import (
    PINECONE_API_KEY,
    PINECONE_INDEX
)

from rag.embeddings import get_embeddings


def get_retriever():

    pc = Pinecone(
        api_key=PINECONE_API_KEY
    )

    index = pc.Index(PINECONE_INDEX)

    vector_store = PineconeVectorStore(
        index=index,
        embedding=get_embeddings()
    )

    return vector_store.as_retriever(
        search_kwargs={"k": 3}
    )