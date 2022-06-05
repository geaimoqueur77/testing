# =============================================================================
# Fonction FizzBuzz
# =============================================================================
def fizzbuzz():
    inf = input("Entrer la borne inférieure de l'intervalle")
    sup = input("Entrer la borne supérieure de l'intervalle")
    while int(sup) <= int(inf):
        sup = input("Entrer la borne supérieure de l'intervalle")
    for i in range(int(inf), int(sup)):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz", end=" ")
        elif i % 3 == 0:
            print("fizz", end=" ")
        elif i % 5 == 0:
            print("buzz", end=" ")
        else:
            print(i, end=" ")


fizzbuzz()
