def multiple(intervalle, nb):
    multiples = []
    for i in intervalle:
        if i % nb == 0:
            multiples.append(i)#ajouter le nombre au tableau 
    return multiples

intervalle=[1,2,3,4,5,6]
print("l'intervalle est: ",intervalle)
print("on va sortir les chiffres multiples par 2 :")
print("la sortie est :", multiple(intervalle,2))