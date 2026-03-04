import os
from dotenv import load_dotenv
load_dotenv()
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

from ingestion import load_tamusa_data

#Chunks documents, creates embeddings, and saves them to a local ChromaDB vector store
def build_vector_store_index(data_directory='./docs', persist_directory='./storage'):
    documents = load_tamusa_data(data_directory)

    #We use 1024 token chunks with a 50 token overlap to ensure context flows
    Settings.node_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=50)

    #Initialize ChromaDB vector store
    db = chromadb.PersistentClient(path=persist_directory)
    chroma_collection = db.get_or_create_collection(name="tamusa_collection")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    #Create the VectorStoreIndex and persist it to disk
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context, show_progress=True)
    return index

#Loads an existing index and returns a retriever object
def get_retriever(index=None, persist_directory='./storage'):

    if index is None:
        db = chromadb.PersistentClient(path=persist_directory)
        chroma_collection = db.get_or_create_collection(name="tamusa_collection")
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    
    return index.as_retriever(similarity_top_k=3)

if __name__ == "__main__":

    #We build the index from our local data and then test the retriever
    # my_index = build_vector_store_index() #Comment this out after the first run to save credits and time since the index is persisted to disk
    retriever = get_retriever(index=None) #Its set to none so that it loads the existing index from disk instead of rebuilding it
