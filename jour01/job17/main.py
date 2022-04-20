
compteur = 0
while compteur < 100:
    compteur += 1
    if (compteur % 5) == 0 and (compteur % 3) == 0:
        print('fizzbuzz')
    elif (compteur % 3) == 0:
        print('fizz')
    elif (compteur % 5) == 0:
        print('buzz')
    else:
        print(compteur)


