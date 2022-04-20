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

def SePresenter(x,y):
    h1 = Personne(x, y)
    h1.setPrenom("Nouveaux prénom")
    h1.setNom("Nouveaux nom")
    h1.display()




print('prenom')
x = input()
print("nom")
y = input()

SePresenter(x,y)