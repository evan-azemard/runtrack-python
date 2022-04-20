class Livre:

    def __init__(self, c_titre):
        self.titre = c_titre

    def print(self):
        print('titre', self.titre)

l = Livre('button')
l.print()

