# =============================================================================
# Fonction de suppression de lettres dans une chaîne de caractère
# =============================================================================
def rmv_letter():
    liste = list()
    chaine = input("Entrez un mot : ")
    if chaine == '':
        print("Fin du programme")
        exit()
    while True:
        elem = input("Entrez une lettre que vous voulez retirer. Tapez sur <ENTER> à vide pour terminer la liste : ")
        if elem != '':
            liste.append(elem)
        else:
            break
    if len(liste) != 0:
        new_str = ''
        for i in range(0, len(chaine)+1):
            x = 0
            for m in liste:
                if chaine[i: i+1] != m:
                    x += 1
                if x == len(liste):
                    new_str = new_str + chaine[i: i+1]
    else:
        new_str = chaine

    print(new_str)

rmv_letter()
