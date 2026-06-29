import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="films", 
    metadata={"hnsw:space": "cosine"}
)

collection.add(
    ids=["f1", "f2", "f3", "f4", "f5"],
    documents=[
        "Un astronaute se perd dans l'espace et tente de survivre",
        "Un détective résout des meurtres dans un Paris des années 1920",
        "Une IA devient consciente et remet en question son existence",
        "Des robots envahissent la Terre et menacent l'humanité",
        "Un enfant découvre un monde magique derrière une armoire",
    ],
    metadatas=[
        {"genre": "sci-fi",   "note": 8.5},
        {"genre": "policier", "note": 7.2},
        {"genre": "sci-fi",   "note": 9.1},
        {"genre": "sci-fi",   "note": 7.8},
        {"genre": "fantaisie","note": 8.0},
    ]
)

# --- Test 1 : query simple ---
print("=== Query simple ===")
r = collection.query(
    query_texts=["film avec des robots et de l'intelligence artificielle"], 
    n_results=2, 
    include=["documents", "distances"]
)

for doc, dist in zip(r["documents"][0], r["distances"][0]):
    print(f"{dist:.4f} {doc}")

# --- Test 2 : query avec filtre métadonnée ---
print("\n=== Query + filtre genre=sci-fi ===")

r = collection.query(
    query_texts=["exploration spatiale"],
    n_results=3,
    where={"genre": "sci-fi"},
    include=["documents", "distances", "metadatas"]
)

for doc, dist, meta in zip(r["documents"][0], r["distances"][0], r["metadatas"][0]):
    print(f"  [{dist:.4f}] (note={meta['note']}) {doc}")


# --- Test 3 : filtre combiné ---
print("\n=== Query + filtre note >= 8.5 ===")
r = collection.query(
    query_texts=["technologie futuriste"],
    n_results=3,
    where={"note": {"$gte": 8.5}},
    include=["documents", "distances", "metadatas"]
)
for doc, dist, meta in zip(r["documents"][0], r["distances"][0], r["metadatas"][0]):
    print(f"  [{dist:.4f}] (note={meta['note']}) {doc}")

# --- Test 4 : deux queries simultanées ---

print("\n=== Deux queries simultanées ===")
r = collection.query(
    query_texts=["crime et enquête", "magie et fantaisie"],
    n_results=2,
    include=["documents", "distances"]
)

for i, query in enumerate(["crime et enquête", "magie et fantaisie"]):
    print(f"\n  Query: '{query}'")
    for doc, dist in zip(r["documents"][i], r["distances"][i]):
        print(f"    [{dist:.4f}] {doc}")




"""
# operateur disponible pour where
where={"note": {"$gte": 8.0}}              # note >= 8.0
where={"genre": {"$in": ["sci-fi", "fantaisie"]}}  # genre dans la liste
where={"$and": [{"genre": "sci-fi"}, {"note": {"$gte": 8.0}}]}  # combinaison
"""


"""

#l2 
collection = client.get_or_create_collection(
    name="films", 
    metadata={"hnsw:space": "l2"}
)

#ip
collection = client.get_or_create_collection(
    name="films",
    metadata={"hnsw:space": "ip"}
)
"""