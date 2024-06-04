Dans ce projet, le fichier de donné de base est 
"[9810000202-sanssymbole-mod.csv](9810000202-sanssymbole-mod.csv)", 
qui est fournis à partir du site d environnement canada. 

La première etape est de générer un fichier .csv avec les données 
traitées pour pouvoir l'exploiter, 
cette étape est réalisé par le programme [preprocess_population_cours.py](preprocess_population_cours.py)
réalisé pendant le cour.

Le fichier [Census_2016_2021.csv](Census_2016_2021.csv) est donc le
document final sur lequel nous pouvons utiliser les différentes données.

Mon analyse de données (rendu du devoir) est donc réalisé dans
le script [main.py](main.py). Le code est concu pour être directement
exécuté, en ayant préalablement installer les modules :
- Pandas
- numpy
- matplotlib

