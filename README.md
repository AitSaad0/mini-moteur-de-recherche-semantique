# 🎬 Mini Moteur de Recherche Sémantique — ChromaDB

Un projet d'apprentissage pour comprendre ChromaDB de zéro : syntaxe de base, CRUD, embeddings et recherche sémantique — **sans LangChain**.

---

## 🎯 Objectifs

- Comprendre les composants fondamentaux de ChromaDB (Client, Collection, Document, Embedding)
- Maîtriser les opérations CRUD sur une collection vectorielle
- Explorer les embeddings et les métriques de similarité (cosine, l2)
- Construire un moteur de recherche sémantique complet avec filtres dynamiques

---

## 🗂️ Structure du projet

```
mini-moteur-de-recherche-semantique/
├── learning/
│   ├── first_coll.py                 # Premier contact avec ChromaDB
│   ├── CRUD_op.py                    # Opérations add, get, update, upsert, delete
│   └── embedding_and_similarite.py   # Métriques cosine/l2, query(), filtres where
│
├── mini-moteur/
│   ├── data.py                       # Dataset de 30 films fictifs
│   ├── setup.py                      # Initialisation et indexation de la collection
│   ├── search.py                     # Moteur de recherche avec filtres dynamiques
│   └── main.py                       # Interface CLI interactive
│
├── chroma_store/                     # Base vectorielle persistée (ignorée par git)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
# Cloner le repo
git clone https://github.com/<username>/mini-moteur-de-recherche-semantique.git
cd mini-moteur-de-recherche-semantique

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

---

## 🚀 Lancement

```bash
# 1. Indexer les 30 films (à faire une seule fois)
python3 mini-moteur/setup.py

# 2. Lancer le moteur de recherche interactif
python3 mini-moteur/main.py
```

**Exemple de session :**

```
🎬 Chargement de la base de films...
✅ Collection déjà chargée (30 films).

🔍 Mini Moteur de Recherche Sémantique
   Commandes : 'q' pour quitter, 'help' pour l'aide

Recherche > robot qui menace l'humanité

── Sans filtre ──
  1. [0.729] Protocole Omega (sci-fi, 2020) ⭐7.9
     Des robots de guerre autonomes se retournent contre leurs créateurs dans un futur proche
  2. [0.543] Chaos Total (comédie, 2023) ⭐7.8
  3. [0.506] Singularité (sci-fi, 2022) ⭐9.1

── Note ≥ 8.0 ──
  1. [0.506] Singularité (sci-fi, 2022) ⭐9.1
     Une IA militaire devient consciente et décide de protéger l'humanité contre elle-même
  ...
```

---

## 🧠 Concepts couverts

### Architecture ChromaDB

```
Client
  └── Collection
        └── Document
              ├── id          → identifiant unique
              ├── document    → texte brut
              ├── embedding   → vecteur [0.12, -0.45, 0.87, ...]
              └── metadata    → {"genre": "sci-fi", "note": 8.5}
```

### Métriques de distance

| Métrique | Range | Cas d'usage |
|----------|-------|-------------|
| `cosine` | 0 → 2 | Texte — mesure l'angle, insensible à la longueur |
| `l2`     | 0 → ∞ | Données numériques — mesure la magnitude |
| `ip`     | -∞ → ∞ | Embeddings normalisés |

### Opérations CRUD

```python
# Add
collection.add(ids=[...], documents=[...], metadatas=[...])

# Get
collection.get(ids=["f1"], include=["documents", "embeddings"])

# Update (remplace) / Upsert (update or insert)
collection.update(ids=["f1"], metadatas=[{...}])
collection.upsert(ids=["f1"], documents=["..."], metadatas=[{...}])

# Delete
collection.delete(ids=["f1"])
collection.delete(where={"genre": "sci-fi"})
```

### Recherche sémantique avec filtres

```python
collection.query(
    query_texts=["film de survie dans l'espace"],
    n_results=5,
    where={"$and": [{"genre": "sci-fi"}, {"note": {"$gte": 8.0}}]},
    include=["documents", "metadatas", "distances"]
)
```

---

## 📦 Dépendances

| Package | Rôle |
|---------|------|
| `chromadb` | Base de données vectorielle |
| `sentence-transformers` | Modèles d'embedding |

Modèle utilisé : **`paraphrase-multilingual-MiniLM-L12-v2`** — optimisé pour le français et les langues non-anglaises.

---

## 💾 Persistance

Les données sont stockées dans `./chroma_store/` via `PersistentClient` :

```
chroma_store/
├── chroma.sqlite3       ← IDs, documents, métadonnées
└── [uuid]/
    └── data_level0.bin  ← Index HNSW (vecteurs)
```

L'algorithme **HNSW** (Hierarchical Navigable Small World) permet une recherche par similarité rapide sans comparer chaque vecteur exhaustivement.

---

## 🔗 Lien avec LangChain

Ce projet illustre ce que LangChain abstrait dans un RAG pipeline :

```python
# LangChain (abstraction)
vectorstore = Chroma(collection_name="docs", embedding_function=ef, persist_directory="./store")
vectorstore.similarity_search(query, k=4)

# ChromaDB pur (ce projet)
collection = client.get_or_create_collection(name="docs", embedding_function=ef)
collection.query(query_texts=[query], n_results=4)
```
