# coder la fonction factorielle
def factorielle(n):
    if n == 1:
        return n
    else:
        return n * factorielle(n-1)


print(factorielle(6))
