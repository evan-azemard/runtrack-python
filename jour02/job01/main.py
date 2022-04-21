class Personne:
    """
    Class Personne
    """

    def __init__(self, c_prenom, c_nom):
        print("     création d' un humain")
        self.prenom = c_prenom
        self.nom = c_nom
        print('prénom =>', c_prenom)
        print("nom", c_nom)

    def setPrenom(self, n):
        self.__prenom = n

    def getPrenom(self):
        return self.__prenom

    def setNom(self, n):
        self.__nom = n

    def getNom(self):
        return self.__nom

    def display(self):
        print('     Nouveaux Prénom de h1 =>', self.getPrenom())
        print('     Nouveaux Nom de h1 =>', self.getNom())


print("lancement programe...")

"""
    classe Livre
"""


class Livre:

    def __init__(self, c_titre):
        self.titre = c_titre

    def print(self):
        print('titre', self.titre)


l = Livre('test')
l.print()

"""
    Class auteur
"""


class Auteur(Personne):
    def setOeuvre(self, n):
        self.__oeuvre = n

    def getOeuvre(self):
        return self.__oeuvre

    def listerOeuvre(self):
        print(self.__oeuvre)

    def ecrireUnLivre(self):
        def setTitre(self, n):
            self.__titre = n

        def getTitre(self):
            return self.__titre

# instance = Auteur()
# instance.ecrireUnLivre()
