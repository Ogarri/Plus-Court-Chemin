from TasFibonacci import TasFibonacci

# Implémentation de l'algorithme de Dijkstra
def dijkstra(graphe, source):
    # Initialisation des distances et des précédents
    # Tous les sommets ont une distance infinie sauf la source qui a une distance de 0
    distances = {sommet: float('inf') for sommet in graphe}
    precedents = {sommet: None for sommet in graphe}
    distances[source] = 0

    # Initialisation du tas de Fibonacci avec tous les sommets
    file = TasFibonacci()
    noeuds = {sommet: file.inserer(distances[sommet], sommet) for sommet in graphe}

    # Boucle principale de l'algorithme
    while file.total_noeuds > 0:
        # Extraction du sommet avec la distance minimale
        noeud_courant = file.extraire_min()
        if noeud_courant is None: 
            break
        distance_courante, sommet_courant = noeud_courant.cle, noeud_courant.valeur

        # Ignorer les distances obsolètes
        if distance_courante > distances[sommet_courant]:
            continue

        # Mise à jour des distances pour les voisins
        for voisin, poids in graphe[sommet_courant]:
            # Calcul de la distance alternative
            alternative = distances[sommet_courant] + poids
            if alternative < distances[voisin]:
                # Mise à jour si une distance plus courte est trouvée
                distances[voisin] = alternative
                precedents[voisin] = sommet_courant
                file.diminuer_cle(noeuds[voisin], alternative)

    return distances, precedents

# Fonction pour reconstruire le chemin à partir des précédents
def reconstruire_chemin(precedents, cible):
    chemin = []
    courant = cible
    while courant is not None:
        chemin.append(courant)
        courant = precedents[courant]
    chemin.reverse()
    return chemin

'''
# Exemple de graphe
graphe = {
    'V1': [('V2', 14), ('V3', 9), ('V4', 7)],
    'V2': [('V1', 14), ('V5', 9)],
    'V3': [('V3', 9), ('V4', 11), ('V6', 10)],
    'V4': [('V1', 7), ('V3', 11), ('V6', 15)],
    'V5': [('V2', 9), ('V6', 6)],
    'V6': [('V3', 10), ('V4', 15), ('V5', 6)]
}

# Exécution de l'algorithme
distances, precedents = dijkstra(graphe, 'V1')

# Affichage des résultats
print("Distances :", distances)
for sommet in graphe:
    print(f"Chemin vers {sommet} :", reconstruire_chemin(precedents, sommet))
'''