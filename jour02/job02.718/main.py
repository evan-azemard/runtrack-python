class Personne():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Client(Personne):
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


class Bibliotheque():
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = []

    def acheterUnLivre(self, auteur, nom, nb):
        livre = Bibliotheque(nom, self)
        self.catalogue.append(livre.titre)

    def inventaire(self, nom, catalogue):
        return print(nom, catalogue)

    def louer(self, instance):
        return print(instance)

    def rendreLivre(self, client):
        self.catalogue.append(client.titre)


instance = Client("nom", "prenom")
instance2 = Bibliotheque()
intance2.louer(instance)
