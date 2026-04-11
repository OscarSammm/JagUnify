import os
import shutil
from dotenv import load_dotenv
load_dotenv()

# Always resolve storage relative to this file so it works regardless of where you run from
_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_STORAGE = os.path.join(_SRC_DIR, 'storage')
_DEFAULT_DATA = os.path.join(_SRC_DIR, '..', 'data', 'techdep_data', 'catalog.jsonl')
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

from ingestion import load_jsonl_data

#Chunks documents, creates embeddings, and saves them to a local ChromaDB vector store
def build_vector_store_index(data_path=_DEFAULT_DATA, persist_directory=_DEFAULT_STORAGE):
    documents = load_jsonl_data(data_path)

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

#Loads an existing persisted index from ChromaDB
def load_index(persist_directory=_DEFAULT_STORAGE):
    db = chromadb.PersistentClient(path=persist_directory)
    chroma_collection = db.get_or_create_collection(name="tamusa_collection")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    return VectorStoreIndex.from_vector_store(vector_store=vector_store)

#Returns a retriever for standalone use or testing
def get_retriever(index=None, similarity_top_k=7, persist_directory=_DEFAULT_STORAGE):
    if index is None:
        index = load_index(persist_directory)
    return index.as_retriever(similarity_top_k=similarity_top_k)

if __name__ == "__main__":
    # Wipe existing storage for a clean rebuild — prevents old chunks mixing with new data
    if os.path.exists(_DEFAULT_STORAGE):
        shutil.rmtree(_DEFAULT_STORAGE)
        print("Cleared existing storage.")

    my_index = build_vector_store_index(_DEFAULT_DATA)
    print("Index built successfully.")