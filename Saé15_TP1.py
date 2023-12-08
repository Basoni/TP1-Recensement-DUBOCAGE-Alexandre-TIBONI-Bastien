import csv
import matplotlib.pyplot as plt

# Fonction pour charger les données d'une ville spécifique à partir du fichier CSV
def charger_donnees_ville(nom_ville, nom_fichier):
    donnees_ville = []
    with open(nom_fichier, newline='') as csvfile:
        delimiter = ','  # Par défaut, utilisation de la virgule comme séparateur
        if nom_fichier.startswith('donnees_2021'):  # Changer le délimiteur pour 2021
            delimiter = ';'
        reader = csv.reader(csvfile, delimiter=delimiter)
        for row in reader:
            if '2021' in nom_fichier and len(row) >= 3 and nom_ville in row[2]:
                donnees_ville.append(row)
            elif len(row) >= 7 and nom_ville in row[6]:
                donnees_ville.append(row)
    return donnees_ville


# Charger les données pour Auxerre des fichiers CSV
donnees_2008 = charger_donnees_ville('Auxerre', 'donnees_2008.csv')
donnees_2016 = charger_donnees_ville('Auxerre', 'donnees_2016.csv')
donnees_2021 = charger_donnees_ville('89024', 'donnees_2021.csv')

# Extraction des populations pour Auxerre pour chaque année
populations = [
    int(donnees_2008[0][7]) if donnees_2008 else 0,  # Utilisation de la 8ème colonne pour 2008 (population totale)
    int(donnees_2016[0][7]) if donnees_2016 else 0,  # Utilisation de la 8ème colonne pour 2016 (population municipale)
    int(donnees_2021[0][3]) if donnees_2021 else 0   # Utilisation de la 4ème colonne pour 2021 (population municipale)
]
print(donnees_2008,donnees_2016,donnees_2021)
# Création de la liste d'années
annees = ['2008', '2016', '2021']

# Tracé du graphique avec les données
plt.plot(annees, populations, marker='o')
plt.title('Évolution de la population d\'Auxerre')
plt.xlabel('Années')
plt.ylabel('Population municipale')
plt.grid(True)
plt.show()