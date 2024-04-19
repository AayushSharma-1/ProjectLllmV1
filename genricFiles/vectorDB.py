import os
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
def vectorDB(index_name, api_key, embeddings, create_vector = False):
    os.environ['PINECONE_API_KEY'] = api_key
    index = PineconeVectorStore(embedding = embeddings, index_name = index_name)
    return index