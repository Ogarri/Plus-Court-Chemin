import random

def generer_graphe(nb_sommets, nb_aretes, poids_min=1, poids_max=10):
    """
    Génère un graphe aléatoire représenté sous forme de dictionnaire.

    :param nb_sommets: Nombre de sommets dans le graphe
    :param nb_aretes: Nombre d'arêtes dans le graphe
    :param poids_min: Poids minimum des arêtes
    :param poids_max: Poids maximum des arêtes
    :return: Un graphe sous forme de dictionnaire {sommet: [(voisin, poids), ...]}
    """
    graphe = {f'V{i}': [] for i in range(1, nb_sommets + 1)}
    aretes = set()

    while len(aretes) < nb_aretes:
        u = f'V{random.randint(1, nb_sommets)}'
        v = f'V{random.randint(1, nb_sommets)}'
        if u != v and (u, v) not in aretes and (v, u) not in aretes:
            poids = random.randint(poids_min, poids_max)
            graphe[u].append((v, poids))
            graphe[v].append((u, poids))  # Supposons un graphe non orienté
            aretes.add((u, v))

    return graphe

# Exemple d'utilisation
if __name__ == "__main__":
    graphe = generer_graphe(6, 10)
    print(graphe)
