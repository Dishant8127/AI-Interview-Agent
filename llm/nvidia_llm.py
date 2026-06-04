from langchain_nvidia_ai_endpoints import ChatNVIDIA

from config.settings import NVIDIA_API_KEY


def get_llm():

    llm = ChatNVIDIA(
        model="meta/llama-3.1-70b-instruct",
        api_key=NVIDIA_API_KEY,
        temperature=0.7
    )

    return llm