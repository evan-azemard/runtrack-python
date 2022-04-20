def arrond(x):
    for i in range (0, len(x)):
        if (x[i] % 5 == 0):
            print(x[i])
        elif ((x[i] +2) % 5 == 0):
            print(x[i]+2)
        else:
            print(x[i])


tabl = [1,12,33,25,18]
arrond(tabl)