import math

print("rentrer un nombre entier")

n = input()
n = int(n)


def fact(n):
    """Recursive function to find factorial"""
    if n == 1:
        return 1
    else:
        return (n * fact(n - 1))


print("Factorial de", n, ":", fact(n))
