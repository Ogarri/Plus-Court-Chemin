from TasMin import TasMin

def dijkstra(graphe, source):
    # Initialisation
    distances = {sommet: float('inf') for sommet in graphe}
    distances[source] = 0
    predecesseurs = {sommet: None for sommet in graphe}
    tas = TasMin()
    tas.ajouter((0, source))  # (distance, sommet)

    while not tas.est_vide():
        distance_actuelle, sommet_actuel = tas.retirer()

        # Vérification pour éviter de traiter des distances obsolètes
        if distance_actuelle > distances[sommet_actuel]:
            continue

        # Correction : itérer sur les voisins et leurs poids
        for voisin, poids in graphe[sommet_actuel]:
            nouvelle_distance = distance_actuelle + poids
            if nouvelle_distance < distances[voisin]:
                distances[voisin] = nouvelle_distance
                predecesseurs[voisin] = sommet_actuel
                tas.ajouter((nouvelle_distance, voisin))

    return distances, predecesseurs

def reconstruire_chemin(predecesseurs, sommet):
    chemin = []
    while sommet is not None:
        chemin.insert(0, sommet)
        sommet = predecesseurs[sommet]
    return chemin

'''
# Correction : structure correcte pour le graphe
graphe = {
    'V1': [('V2', 14), ('V3', 9), ('V4', 7)],
    'V2': [('V1', 14), ('V5', 9)],
    'V3': [('V4', 11), ('V6', 10)],
    'V4': [('V1', 7), ('V3', 11), ('V6', 15)],
    'V5': [('V2', 9), ('V6', 6)],
    'V6': [('V3', 10), ('V4', 15), ('V5', 6)]
}

#Execution de l'algorithme
distances, predecesseurs = dijkstra(graphe, 'V1')

#Affichage des résultats
print("Distances :", distances)
for sommet in graphe:
    print(f"Chemin vers {sommet} :", reconstruire_chemin(predecesseurs, sommet))
'''