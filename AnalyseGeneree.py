from GenerateGraph import generer_graphe
from DijkstraFibo import dijkstra as dijkstra_fibo
from DiijkstraMin import dijkstra as dijkstra_min
from BellmanFord import bellman_ford
import time

def analyser_algorithmes(nb_sommets, nb_aretes):
    # Générer un graphe aléatoire
    graphe = generer_graphe(nb_sommets, nb_aretes)
    source = list(graphe.keys())[0]  # Choisir un sommet source arbitraire

    print(f"Graphe généré avec {nb_sommets} sommets et {nb_aretes} arêtes :")
    print(graphe)

    # Analyse de Dijkstra avec Tas de Fibonacci
    debut = time.time()
    distances_fibo, _ = dijkstra_fibo(graphe, source)
    fin = time.time()
    print("\nDijkstra (Tas Fibonacci) :")
    print("Distances :", distances_fibo)
    print(f"Temps d'exécution : {fin - debut:.6f} secondes")

    # Analyse de Dijkstra avec Tas Min
    debut = time.time()
    distances_min, _ = dijkstra_min(graphe, source)
    fin = time.time()
    print("\nDijkstra (Tas Min) :")
    print("Distances :", distances_min)
    print(f"Temps d'exécution : {fin - debut:.6f} secondes")

    # Analyse de Bellman-Ford
    debut = time.time()
    try:
        precedents_bf = bellman_ford(graphe, source)
        distances_bf = {v: float('inf') for v in graphe}
        distances_bf[source] = 0
        for v in precedents_bf:
            if precedents_bf[v] is not None:
                distances_bf[v] = distances_bf[precedents_bf[v]] + \
                                  next(p for u, p in graphe[precedents_bf[v]] if u == v)
        print("\nBellman-Ford :")
        print("Distances :", distances_bf)
    except ValueError as e:
        print("\nBellman-Ford :")
        print("Erreur :", e)
    fin = time.time()
    print(f"Temps d'exécution : {fin - debut:.6f} secondes")

# Exemple d'utilisation
if __name__ == "__main__":
    analyser_algorithmes(6, 10)
