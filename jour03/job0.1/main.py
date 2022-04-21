print("rentrer un nombre entier")

n = input()
n = int(n)
x = 5


def calc(x, n):
    if n == 0 or n == 1:
        return x
    else:
        return x * calc(x, n - 1)


print(calc(x, n))
