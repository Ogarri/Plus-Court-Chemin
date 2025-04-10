# SAE Algo4 - Plus Court Chemin

Ce projet implémente plusieurs algorithmes pour résoudre le problème du plus court chemin dans un graphe pondéré. Les algorithmes incluent Dijkstra (avec Tas Min et Tas Fibonacci) et Bellman-Ford. Le projet permet également de générer des graphes aléatoires et d'analyser les performances des algorithmes.

## Structure des fichiers

### 1. **BellmanFord.py**
Implémente l'algorithme de Bellman-Ford pour trouver les distances minimales depuis un sommet source. Détecte également les cycles de poids négatif.

### 2. **TasMin.py**
Implémente un tas binaire minimum pour gérer efficacement les priorités dans l'algorithme de Dijkstra.

### 3. **TasFibonacci.py**
Implémente un tas de Fibonacci, une structure de données avancée utilisée pour optimiser l'algorithme de Dijkstra.

### 4. **DiijkstraMin.py**
Implémente l'algorithme de Dijkstra en utilisant un tas binaire minimum (`TasMin`).

### 5. **DijkstraFibo.py**
Implémente l'algorithme de Dijkstra en utilisant un tas de Fibonacci (`TasFibonacci`).

### 6. **GenerateGraph.py**
Permet de générer des graphes aléatoires avec un nombre donné de sommets et d'arêtes. Les graphes sont représentés sous forme de dictionnaires.

### 7. **AnalyseGeneree.py**
Compare les performances des algorithmes (Dijkstra avec Tas Fibonacci, Dijkstra avec Tas Min, et Bellman-Ford) sur des graphes générés aléatoirement.

### 8. **Analyse.py**
Lit un graphe à partir d'un fichier CSV et compare les performances des algorithmes sur ce graphe. Ce fichier est utile pour analyser des graphes réels.

### 9. **.gitignore**
Ignore les fichiers CSV générés ou utilisés dans le projet.

## Exécution

### Génération de graphes
Pour générer un graphe aléatoire, exécutez le fichier `GenerateGraph.py` :
```bash
python GenerateGraph.py
```

### Analyse des algorithmes
Pour comparer les performances des algorithmes sur des graphes générés aléatoirement :
```bash
python AnalyseGeneree.py
```

Pour analyser un graphe à partir d'un fichier CSV :
1. Placez le fichier CSV dans le dossier `CSV/`.
2. Modifiez le chemin du fichier dans `Analyse.py`.
3. Exécutez le fichier :
   ```bash
   python Analyse.py
   ```

## Dépendances
Aucune bibliothèque externe n'est requise. Le projet utilise uniquement des modules standard de Python.

## Contributions
Les contributions sont les bienvenues. Veuillez soumettre une pull request ou signaler un problème via GitHub.

## Auteurs
Projet réalisé dans le cadre de la SAE Algo4.
