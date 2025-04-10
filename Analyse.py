import csv
import time

def lire_graphe_depuis_csv(fichier_csv):
    graphe = {}
    with open(fichier_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sommet = row['place1']
            voisin = row['place2']
            poids = float(row['mi_to_place'])
            if sommet not in graphe:
                graphe[sommet] = []
            graphe[sommet].append((voisin, poids))
    return graphe

if __name__ == "__main__":
    from DijkstraFibo import dijkstra as dijkstra_fibo
    from DiijkstraMin import dijkstra as dijkstra_min
    from BellmanFord import bellman_ford

    # Lecture du graphe depuis un fichier CSV
    fichier_csv = "CSV/gaz1990placedistance25miles.csv"  # Remplacez par le chemin réel du fichier CSV
    graphe_consequent = lire_graphe_depuis_csv(fichier_csv)

    # Vérification de l'existence du sommet de départ
    sommet_depart = 'V1'
    if sommet_depart not in graphe_consequent:
        print(f"Erreur : Le sommet de départ '{sommet_depart}' n'existe pas dans le graphe.")
        sommet_depart = next(iter(graphe_consequent))  # Choisir un sommet valide par défaut
        print(f"Utilisation du sommet '{sommet_depart}' comme sommet de départ.")

    # Test avec l'algorithme utilisant le tas de Fibonacci
    print("Test avec le tas de Fibonacci")
    start_fibo = time.time()
    distances_fibo, _ = dijkstra_fibo(graphe_consequent, sommet_depart)
    print("Distances calculées (Fibonacci):", distances_fibo)
    end_fibo = time.time()

    # Test avec l'algorithme utilisant le tas binaire
    print("\nTest avec le tas binaire")
    start_min = time.time()
    distances_min, _ = dijkstra_min(graphe_consequent, sommet_depart)
    print("Distances calculées (Min):", distances_min)
    end_min = time.time()

    print("\nTest avec l'algorithme de Bellman-Ford")
    start_bf = time.time()
    resultats_bellman = bellman_ford(graphe_consequent, sommet_depart)
    if len(resultats_bellman) == 2:
        distance_bellman, _ = resultats_bellman
    else:
        distance_bellman = resultats_bellman  # Si une seule valeur est retournée
    print("Distances calculées (Bellman-Ford):", distance_bellman)
    end_bf = time.time()

    print("\nTemps d'exécution :")
    print(f"Fibonacci : {end_fibo - start_fibo:.6f} secondes")
    print(f"Min : {end_min - start_min:.6f} secondes")
    print(f"Bellman-Ford : {end_bf - start_bf:.6f} secondes")

'''
Analyse théorique de la complexité : Déterminez, pour chacune des implémentations,
une borne asymptotique supérieure O du temps d’exécution en fonction du nombre de
sommets et d’arêtes. Justifiez rigoureusement chaque étape de votre raisonnement.
'''

'''
Analyse empirique : Testez les deux implémentations sur un jeu de données pertinent
et accessible en ligne. Décrivez en détail le jeu de données utilisé et citez vos sources.
Présentez ensuite vos résultats sous forme de graphiques, en comparant les performances
observées aux bornes théoriques établies.
'''
