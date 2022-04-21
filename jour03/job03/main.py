print("Entrer un entier")
n = input()
n = int(n)


def table(width):
    x = " O " * (width - 1)
    y = "X "
    for i in range(1, width):
        print(x, y)


table(n)
