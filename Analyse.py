# Création d'un graphe conséquent avec 100 sommets et des arêtes aléatoires
import random
import time

def generer_graphe_consequent(nombre_sommets, max_poids):
    graphe = {}
    for i in range(1, nombre_sommets + 1):
        sommet = f'V{i}'
        graphe[sommet] = []
        for _ in range(random.randint(1, 10)):  # Chaque sommet a entre 1 et 10 voisins
            voisin = f'V{random.randint(1, nombre_sommets)}'
            if voisin != sommet:  # Éviter les boucles
                poids = random.randint(1, max_poids)
                graphe[sommet].append((voisin, poids))
    return graphe

# Génération d'un graphe conséquent avec 1000 sommets
graphe_consequent = generer_graphe_consequent(1000, 20)

# Sauvegarde du graphe pour les tests
if __name__ == "__main__":
    from DijkstraFibo import dijkstra as dijkstra_fibo
    from DiijkstraMin import dijkstra as dijkstra_min

    # Test avec l'algorithme utilisant le tas de Fibonacci
    print("Test avec le tas de Fibonacci")
    start_fibo = time.time()
    distances_fibo, _ = dijkstra_fibo(graphe_consequent, 'V1')
    print("Distances calculées (Fibonacci):", distances_fibo)
    end_fibo = time.time()

    # Test avec l'algorithme utilisant le tas binaire
    print("\nTest avec le tas binaire")
    start_min = time.time()
    distances_min, _ = dijkstra_min(graphe_consequent, 'V1')
    print("Distances calculées (Min):", distances_min)
    end_min = time.time()

    print("\nTemps d'exécution :")
    print(f"Fibonacci : {end_fibo - start_fibo:.6f} secondes")
    print(f"Min : {end_min - start_min:.6f} secondes")