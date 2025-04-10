import math

class TasFibonacci:

    class Noeud:
        def __init__(self, cle, valeur):
            # Initialisation d'un nœud du tas
            self.cle = cle
            self.valeur = valeur
            self.parent = self.enfant = self.gauche = self.droite = None
            self.degre = 0
            self.marque = False

    def __init__(self):
        self.noeuds = []  # Initialisation de la liste des nœuds
        self.noeud_min = None  # Référence au nœud avec la clé minimale

    def iterer(self, tete):
        # Itération optimisée sur les nœuds d'une liste circulaire
        if tete is None:
            return
        noeud = tete
        while True:
            yield noeud
            noeud = noeud.droite
            if noeud == tete:
                break

    liste_racine, noeud_min = None, None
    total_noeuds = 0

    def trouver_min(self):
        # Retourne le nœud avec la clé minimale
        return self.noeud_min

    def extraire_min(self):
        # Extrait le nœud avec la clé minimale
        z = self.noeud_min
        if z is not None:
            if z.enfant is not None:
                enfants = [x for x in self.iterer(z.enfant)]
                for i in range(0, len(enfants)):
                    self.fusionner_avec_liste_racine(enfants[i])
                    enfants[i].parent = None
            self.retirer_de_liste_racine(z)
            if z == z.droite:
                self.noeud_min = self.liste_racine = None
            else:
                self.noeud_min = z.droite
                self.consolider()
            self.total_noeuds -= 1
        return z

    def inserer(self, cle, valeur=None):
        # Insère un nouveau nœud dans le tas
        n = self.Noeud(cle, valeur)
        n.gauche = n.droite = n
        self.fusionner_avec_liste_racine(n)
        if self.noeud_min is None or n.cle < self.noeud_min.cle:
            self.noeud_min = n
        self.total_noeuds += 1
        return n

    def diminuer_cle(self, x, k):
        # Diminue la clé d'un nœud
        if k > x.cle:
            return None
        x.cle = k
        y = x.parent
        if y is not None and x.cle < y.cle:
            self.couper(x, y)
            self.coupe_cascade(y)
        if self.noeud_min is None or x.cle < self.noeud_min.cle:
            self.noeud_min = x

    def fusionner(self, tas2):
        # Fusionne deux tas de Fibonacci
        if tas2.liste_racine is None:
            return self
        if self.liste_racine is None:
            self.liste_racine = tas2.liste_racine
            self.noeud_min = tas2.noeud_min
            self.total_noeuds = tas2.total_noeuds
            return self

        dernier_self = self.liste_racine.gauche
        premier_tas2 = tas2.liste_racine
        dernier_tas2 = tas2.liste_racine.gauche

        dernier_self.droite = premier_tas2
        premier_tas2.gauche = dernier_self
        dernier_tas2.droite = self.liste_racine
        self.liste_racine.gauche = dernier_tas2

        if tas2.noeud_min.cle < self.noeud_min.cle:
            self.noeud_min = tas2.noeud_min

        self.total_noeuds += tas2.total_noeuds
        return self

    def couper(self, x, y):
        # Coupe le lien entre un nœud et son parent
        self.retirer_de_liste_enfants(y, x)
        y.degre -= 1
        self.fusionner_avec_liste_racine(x)
        x.parent = None
        x.marque = False

    def coupe_cascade(self, y):
        # Effectue une coupe en cascade
        z = y.parent
        if z is not None:
            if y.marque is False:
                y.marque = True
            else:
                self.couper(y, z)
                self.coupe_cascade(z)

    def consolider(self):
        max_degre = 0
        # Calculer le degré maximum possible
        for noeud in self.noeuds:
            max_degre = max(max_degre, noeud.degre)

        # Ajuster la taille de A dynamiquement
        taille_A = max_degre + 1
        A = [None] * taille_A

        for noeud in self.noeuds:
            d = noeud.degre
            while d >= len(A):  # Ajuster la taille si nécessaire
                A.append(None)
            while A[d] is not None:
                autre = A[d]
                if noeud.cle > autre.cle:
                    noeud, autre = autre, noeud
                self.lier(autre, noeud)
                A[d] = None
                d += 1
                while d >= len(A):  # Ajuster la taille si nécessaire
                    A.append(None)
            A[d] = noeud

        self.noeud_min = None
        for i in range(len(A)):
            if A[i] is not None:
                if self.noeud_min is None or A[i].cle < self.noeud_min.cle:
                    self.noeud_min = A[i]

    def lier(self, y, x):
        # Lie deux nœuds en faisant de y un enfant de x
        self.retirer_de_liste_racine(y)
        y.gauche = y.droite = y
        self.fusionner_avec_liste_enfants(x, y)
        x.degre += 1
        y.parent = x
        y.marque = False

    def fusionner_avec_liste_racine(self, noeud):
        # Fusion optimisée d'un nœud avec la liste des racines
        if self.liste_racine is None:
            self.liste_racine = noeud
        else:
            noeud.droite = self.liste_racine
            noeud.gauche = self.liste_racine.gauche
            self.liste_racine.gauche.droite = noeud
            self.liste_racine.gauche = noeud

    def fusionner_avec_liste_enfants(self, parent, noeud):
        # Fusionne un nœud avec la liste des enfants d'un parent
        if parent.enfant is None:
            parent.enfant = noeud
        else:
            noeud.droite = parent.enfant.droite
            noeud.gauche = parent.enfant
            parent.enfant.droite.gauche = noeud
            parent.enfant.droite = noeud

    def retirer_de_liste_racine(self, noeud):
        # Retrait optimisé d'un nœud de la liste des racines
        if noeud == self.liste_racine and noeud.droite == noeud:
            self.liste_racine = None
        else:
            noeud.gauche.droite = noeud.droite
            noeud.droite.gauche = noeud.gauche
            if noeud == self.liste_racine:
                self.liste_racine = noeud.droite

    def retirer_de_liste_enfants(self, parent, noeud):
        # Retire un nœud de la liste des enfants d'un parent
        if parent.enfant == parent.enfant.droite:
            parent.enfant = None
        elif parent.enfant == noeud:
            parent.enfant = noeud.droite
            noeud.droite.parent = parent
        noeud.gauche.droite = noeud.droite
        noeud.droite.gauche = noeud.gauche
