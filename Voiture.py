class Voiture:
    def __init__(self, v_marque, v_modele, v_couleur):
        self.marque = v_marque
        self.modele = v_modele
        self.couleur = v_couleur
        self.proprietaire = None

    def affichier(self):
        print('Cettte voiture est:', self.marque, self.modele, self.couleur, 'et elle est à ', self.proprietaire)


