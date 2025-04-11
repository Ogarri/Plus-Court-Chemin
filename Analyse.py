import csv
import time
import matplotlib.pyplot as plt  # Ajout pour les graphiques

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

    # Affichage du nombre de sommets et d'arêtes
    nombre_sommets = len(graphe_consequent)
    nombre_aretes = sum(len(voisins) for voisins in graphe_consequent.values())
    print(f"Nombre de sommets : {nombre_sommets}")
    print(f"Nombre d'arêtes : {nombre_aretes}")

    # Données pour les graphiques
    algorithmes = ['Fibonacci', 'Min', 'Bellman-Ford']
    temps_execution = [end_fibo - start_fibo, end_min - start_min, end_bf - start_bf]

    # Tracé des graphiques
    plt.figure(figsize=(10, 6))
    plt.bar(algorithmes, temps_execution, color=['blue', 'green', 'red'])
    plt.xlabel('Algorithmes')
    plt.ylabel('Temps d\'exécution (secondes)')
    plt.title('Comparaison des temps d\'exécution des algorithmes')
    plt.show()

    # Exemple de borne théorique (O(n log n) pour Dijkstra avec tas de Fibonacci)
    borne_theorique_fibo = [nombre_sommets * (nombre_aretes ** 0.5)]  # Exemple simplifié
    borne_theorique_min = [nombre_sommets * nombre_aretes]  # Exemple simplifié
    borne_theorique_bf = [nombre_sommets * nombre_aretes]  # Exemple simplifié

    # Comparaison des performances observées avec les bornes théoriques
    plt.figure(figsize=(10, 6))
    plt.plot(algorithmes, temps_execution, label='Temps observés', marker='o')
    plt.plot(algorithmes, [borne_theorique_fibo[0], borne_theorique_min[0], borne_theorique_bf[0]], 
             label='Borne théorique', linestyle='--', marker='x')
    plt.xlabel('Algorithmes')
    plt.ylabel('Temps (secondes)')
    plt.title('Comparaison des performances observées et théoriques')
    plt.legend()
    plt.show()

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
