class TasMin:
    def __init__(self):
        # Initialisation du tas sous forme de liste
        self.tas = []

    def ajouter(self, element):
        # Ajout d'un élément au tas et réorganisation
        self.tas.append(element)
        self._tamiser_haut(len(self.tas) - 1)

    def retirer(self):
        # Retrait de l'élément minimum (racine) du tas
        if not self.tas:
            return None
        self._echanger(0, len(self.tas) - 1)
        element_min = self.tas.pop()
        self._tamiser_bas(0)
        return element_min

    def _tamiser_haut(self, index):
        # Réorganisation du tas après ajout d'un élément
        parent = (index - 1) // 2
        while index > 0 and self.tas[index][0] < self.tas[parent][0]:
            self._echanger(index, parent)
            index = parent
            parent = (index - 1) // 2

    def _tamiser_bas(self, index):
        # Réorganisation du tas après retrait de l'élément minimum
        enfant = 2 * index + 1
        while enfant < len(self.tas):
            droit = enfant + 1
            if droit < len(self.tas) and self.tas[droit][0] < self.tas[enfant][0]:
                enfant = droit
            if self.tas[index][0] <= self.tas[enfant][0]:
                break
            self._echanger(index, enfant)
            index = enfant
            enfant = 2 * index + 1

    def _echanger(self, i, j):
        # Échange de deux éléments dans le tas
        self.tas[i], self.tas[j] = self.tas[j], self.tas[i]

    def est_vide(self):
        # Vérifie si le tas est vide
        return len(self.tas) == 0

    def mettre_a_jour(self, element):
        # Met à jour un élément dans le tas
        for i, (valeur, sommet) in enumerate(self.tas):
            if sommet == element[1]:
                self.tas[i] = element
                self._tamiser_haut(i)
                self._tamiser_bas(i)
                break
    
