class Personne:
    def __init__(self, p_nom, p_prenom, p_age):
        self.nom = p_nom
        self.prenom = p_prenom
        self.age = p_age

    def afficher(self):
        print('Je suis ', self.prenom, 'et j ai', self.age)