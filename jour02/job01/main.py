class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):

    def __init__(self, nom, prenom):
        self.oeuvre = []

    def listerOeuvre(self):
        print(self.oeuvre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre.titre)


class Livre():

    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    # def fprint(self):
    #     return print(self.titre)


# Auteur
LivreAut = Auteur("Auteur1", "Auteur2")

# print
# LivreAut.fprint()

# Livre
LivreAut.ecrireUnLivre("Titre1")

LivreAut.ecrireUnLivre("Titre2")

# Lister
LivreAut.listerOeuvre()
