def bellman_ford(graph, source):
    """
    Implémente l'algorithme de Bellman-Ford pour trouver les distances minimales
    depuis un sommet source vers tous les autres sommets d'un graphe pondéré.

    :param graph: Dictionnaire représentant le graphe {u: [(v, poids), ...]}
    :param source: Sommet source
    :return: Dictionnaire des prédécesseurs pour reconstruire les chemins
    """
    # Initialisation
    dist = {v: float('inf') for v in graph}
    precedent = {v: None for v in graph}
    dist[source] = 0

    # Relaxation des arêtes
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, poids in graph[u]:
                if dist[u] + poids < dist[v]:
                    dist[v] = dist[u] + poids
                    precedent[v] = u

    # Détection de cycles négatifs
    for u in graph:
        for v, poids in graph[u]:
            if dist[u] + poids < dist[v]:
                raise ValueError("Le graphe contient un cycle de poids négatif.")

    return precedent
