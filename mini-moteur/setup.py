import chromadb
from chromadb.utils import embedding_functions
from data import FILMS

def init_collection():
    client = chromadb.PersistentClient(path="./chroma_store")
    
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
         model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )

    collection = client.get_or_create_collection(
        name="films", 
        embedding_function=ef, 
        metadata={"hnsw:space": "cosine"}
    )

    if collection.count() == 0:
        collection.add(
            ids=[f["id"] for f in FILMS], 
            documents=[f["description"] for f in FILMS], 
            metadatas=[{
                 "titre":  f["titre"],
                "genre":  f["genre"],
                "note":   f["note"],
                "année":  f["année"]
            } for f in FILMS]
        )
        print(f"✅ {collection.count()} films indexés.")
    else:
        print(f"✅ Collection déjà chargée ({collection.count()} films).")

    return collection

if __name__ == "__main__":
    init_collection()