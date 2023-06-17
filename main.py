"""
Une petie révision ::
"""

# Qu'est ce que une classe / Objet ?
# Une classe contient des attributs (data) et des méthodes (comportement / traitement)
# Une classe Est un concept abstrait qui permet de créer des objets concrets
# La classe se trouve dans le fichiers et les objets se trouvent dans la mémoire

# Le constructeur permet de créer des objets

# 4 pliers de l'OO : encapsulation / abstraction / héritage / polymorphisme

#class ::

class Personne:
    def __init__(self, p_nom, p_prenom, p_age):
        self.nom = p_nom
        self.prenom = p_prenom
        self.age = p_age

    def afficher(self):
        print('Je suis ', self.prenom, 'et j ai', self.age)

class Voiture:
    def __init__(self, v_marque, v_modele, v_couleur):
        self.marque = v_marque
        self.modele = v_modele
        self.couleur = v_couleur
        self.proprietaire = None

    def affichier(self):
        print('Cettte voiture est:', self.marque, self.modele, self.couleur, 'et elle est à ', self.proprietaire)

# Création des objets

liste = []
liste.append(Personne('babari', 'raouf', 31))
liste.append(Personne('bachir', 'Fikry', 25))
liste.append(Personne('Nabil', 'Agsous', 40))

# Les objets de la même classe se comportemt souvent de la même manière ...
for x in liste:
    x.afficher()


#Exercice Créer une liste de 4 Voiture
# Trouver un moyen pour informer quelle personne conduit quelle voiture ???

# Création des 4 Voiture
liste_v = []
liste_v.append(Voiture('Subaru','Outback','noir'))
liste_v.append(Voiture('Toyota','Rav4','rouge'))
liste_v.append(Voiture('Nissan','Rougue','jaune'))
liste_v.append(Voiture('Honda','Civic','vert'))

liste_v[0].proprietaire = liste[0].prenom
liste_v[1].proprietaire = liste[1].prenom
liste_v[2].proprietaire = liste[2].prenom
liste_v[3].proprietaire = liste[1].prenom

for x in liste_v:
    x.affichier()

# à corriger
