

#class ::

class Voiture:
    def __init__(self,marque,modele,anne,couleur):
        self.marque = marque
        self.modele = modele
        self.anne = anne
        self.couleur = couleur

    def afficher(self):
        print(self.marque, self.modele, self.anne, self.couleur)

liste= []
liste.append(Voiture('Mazda', 'Cx-30', '2021','rouge'))
liste.append(Voiture('Nissan', 'Rogue', '2022','noir'))
liste.append(Voiture('Honda','CRV', '2023','gris'))

for x in liste:
    x.afficher()