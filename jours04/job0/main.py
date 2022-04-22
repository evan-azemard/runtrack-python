print('Ecrire une string')
x = input()

fichier = open('output.txt', "a")

fichier.write(x)
fichier.close()
