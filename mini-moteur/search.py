def search(collection, query, n=5, genre=None, note_min=None, année_min=None):
    conditions = []

    if genre:
        conditions.append({"genre": genre})
    if note_min is not None:
        conditions.append({"note": {"$gte": note_min}})
    if année_min is not None:
        conditions.append({"année": {"$gte": année_min}})

    if len(conditions) == 0: 
        where = None
    elif len(conditions) == 1: 
        where = conditions[0]
    else: 
        where = {"$and": conditions} 

    results = collection.query(
        query_texts = query, 
        n_results = n, 
        where=where, 
        include=["documents", "metadatas", "distances"]
    )
    films = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        films.append({
            "titre":       meta["titre"],
            "genre":       meta["genre"],
            "note":        meta["note"],
            "année":       meta["année"],
            "description": doc,
            "score":       round(1 - dist, 3)  # similarité : 1=identique, 0=opposé
        })

    return films



def display_results(films):
    if not films:
        print("  Aucun résultat trouvé.")
        return
    for i, f in enumerate(films, 1):
        print(f"\n  {i}. [{f['score']:.3f}] {f['titre']} ({f['genre']}, {f['année']}) ⭐{f['note']}")
        print(f"     {f['description']}")