import chromadb

client = chromadb.Client()

test_coll = client.create_collection(name="test")
collection = client.get_or_create_collection(name="films")

print(client.list_collections())

documents = [
    "Un astronaute se perd dans l'espace et tente de survivre",
    "Un détective résout des meurtres dans un Paris des années 1920",
    "Une IA devient consciente et remet en question son existence",
]

ids = ["f1", "f2", "f3"]

metadatas=[
        {"genre": "sci-fi",  "année": 2023, "note": 8.5},
        {"genre": "policier","année": 2021, "note": 7.2},
        {"genre": "sci-fi",  "année": 2022, "note": 9.1},
]


collection.add(
    documents=documents, 
    ids=ids, 
    metadatas=metadatas
)


#--------------------------------------------------------------
# 1. Get

# Tout récupérer
resultat = collection.get()
print(resultat)

# Par id specifique
resultat = collection.get(ids=["f1", "f2"])
print(resultat)

# Avec les embeddings (masqués par défaut)
resultat = collection.get(
    ids=["f1"], 
    include=["documents", "metadatas", "embeddings"]
)
print(resultat)


# Compter les documents
count = collection.count()
print(count)


#--------------------------------------------------------------
# 2. Update

# update() modifie uniquement les ids qui existent déjà
collection.update(
    ids=["f1"], 
    metadatas=[{"genre": "sci-fi", "année": 2023, "note": 9.0}]  # note changée
)
print("Note f1 après UPDATE :", collection.get(ids=["f1"])["metadatas"])

# upsert() = update() s'il existe ajouter sinon 
collection.upsert(
    ids=["f1", "f4"], 
    documents=[
        "Un astronaute se perd dans l'espace et tente de survivre",
        "Un enfant découvre un monde magique derrière une armoire",
    ],
    metadatas=[
        {"genre": "sci-fi",   "année": 2023, "note": 9.0},
        {"genre": "fantaisie","année": 2020, "note": 8.0},
    ]
)
print("Après UPSERT :", collection.count())  


#--------------------------------------------------------------
# 3. Delete

#Par IDs
collection.delete(
    ids=["f1"]
)
print("Après DELETE :", collection.count())  # 

# Par filtre sur métadonnées
collection.delete(where={"genre": "sci-fi"})

# Supprimer toute la collection
client.delete_collection(name="test")
client.delete_collection(name="films")

