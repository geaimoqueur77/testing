def multiple(intervalle, nb):
    multiples = []
    for i in intervalle:
        if i % nb == 0:
            multiples.append(i)#ajouter le nombre au tableau 
    return multiples

intervalle=[1,2,3,4,5,6]
print(multiple(intervalle,2))