from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

from config.settings import NVIDIA_API_KEY


def get_embeddings():

    embeddings = NVIDIAEmbeddings(
        model="nvidia/nv-embedqa-e5-v5",
        api_key=NVIDIA_API_KEY
    )

    return embeddings