import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# lecture du fichier traité
df = pd.read_csv('Census_2016_2021.csv')

# DataFrame avec uniquement les municipalités
df_municipalites = df[df['Type'] == 'MÉ'].copy() # Ajout de copy pour éviter les modifications du dataframe initial

# Affichage nombre de municipalités
print(f'Nombre de municipalités :{len(df_municipalites)}')

# Calcul de la population moyenne en 2016 et en 2021 pour les municipalités
print(f'Population moyenne des municipalités en 2016 est :{df_municipalites['Pop16'].mean()}')
print(f'Population moyenne des municipalités en 2021 est :{df_municipalites['Pop21'].mean()}')

# Création de la figure et des axes pour les subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 8)) #2 colones : 1 nuage de point et 1 diagramme en barre

# Calcul du pourcentage d'accroissement en fonction de la population en 2021
pourcentage_accroissement = ((df_municipalites['Pop21'] - df_municipalites['Pop16']) / df_municipalites['Pop16']) * 100
axes[0].scatter(df_municipalites['Pop21'], pourcentage_accroissement,color='red')
axes[0].set_xlabel('Population 2021')
axes[0].set_ylabel('% Accroissement de population (2016-2021)')
axes[0].set_title('Accroissement de population en fonction de la population 2021')

# création de la classification des villes
classe_ville = [0, 2000, 9999, 24999, 99999, np.inf]
# légendes à afficher
labels = ['Moins de 2000', '2000 à 9999', '10000 à 24999', '25000 à 99999', '100000 et plus']
# nouveau découpage des municipalité avec nos nouvelles classes
df_municipalites['Population_Category'] = pd.cut(df_municipalites['Pop21'], bins=classe_ville, labels=labels)

# Diagramme en barres horizontales du nombre de municipalités dans chaque catégorie
Nb_villes_categorie = df_municipalites['Population_Category'].value_counts()
Nb_villes_categorie.plot(kind='barh', ax=axes[1], color='red')
axes[1].set_xlabel('Catégorie des municipalités')
axes[1].set_ylabel('Nombre de municipalités')
axes[1].set_title('Nombre de municipalités dans chaque catégorie de population en 2021')

# ajustement automatique
plt.tight_layout()


plt.show()