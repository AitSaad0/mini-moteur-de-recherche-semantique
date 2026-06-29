from setup import init_collection
from search import search, display_results

def main():
    print("🎬 Chargement de la base de films...")
    collection = init_collection()

    print("\n🔍 Mini Moteur de Recherche Sémantique")
    print("   Commandes : 'q' pour quitter, 'help' pour l'aide\n")

    while True:
        query = input("Recherche > ").strip()

        if query == "q":
            break
        if query == "help":
            print("  Exemples :")
            print("  - 'film de survie dans l'espace'")
            print("  - 'thriller psychologique'")
            print("  - 'histoire de famille touchante'")
            continue
        if not query:
            continue

        # Recherche simple
        print("\n── Sans filtre ──")
        films = search(collection, query, n=3)
        display_results(films)

        # Recherche avec filtre note >= 8.0
        print("\n── Note ≥ 8.0 ──")
        films = search(collection, query, n=3, note_min=8.0)
        display_results(films)

        print()

if __name__ == "__main__":
    main()