def inf():
    while True:
        mot = input("ecrire \"stop\" pour sortir")
        if mot != "stop":
            print(mot)
        else:
            break
    print("sortie")
inf()
