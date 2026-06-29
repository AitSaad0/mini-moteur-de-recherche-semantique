import chromadb

# 1. Initialize the ChromaDB client dans la memoire
client = chromadb.Client()

# 2. create a collection 
collection = client.create_collection(name="test_collection")

# 3. Add documents to the collection
collection.add(
    documents=["ChromaDB est une base de données vectorielle"], 
    ids=["docs1"]
)

# 4. faire une recherche 
resultat = collection.query(
    query_texts=["base de donnees vectorielle"], 
    n_results=1
)

print(resultat)



