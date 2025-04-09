class TasMin:
    def __init__(self, tas=[]):
        self.tas = tas
        self.nTas = len(tas)

    def maximum(self):
        # Retourne le maximum du tas (racine pour un tas max)
        if self.nTas == 0:
            return None
        return self.tas[0]

    def ajouter(self, v):
        i = self.nTas
        self.tas.append(v)
        self.nTas += 1
        while i > 0 and self.tas[(i - 1) // 2] <= v:
            self.tas[i] = self.tas[(i - 1) // 2]
            i = (i - 1) // 2
        self.tas[i] = v

    def retirer(self):
        if self.nTas == 0:
            return None
        # Suppression de l'élément minimum (racine du tas)
        minimum = self.tas[0]
        self.tas[0] = self.tas[self.nTas - 1]
        self.nTas -= 1
        del self.tas[self.nTas]
        if self.nTas == 0:
            return minimum
        # Réorganiser le tas pour maintenir la propriété
        i = 0
        while 2 * i + 1 < self.nTas:
            j = 2 * i + 1
            if j + 1 < self.nTas and self.tas[j + 1] < self.tas[j]:
                j += 1
            if self.tas[i] <= self.tas[j]:
                break
            self.tas[i], self.tas[j] = self.tas[j], self.tas[i]
            i = j
        return minimum

    def est_vide(self):
        # Vérifie si le tas est vide
        return self.nTas == 0
