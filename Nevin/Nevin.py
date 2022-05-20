nevin = list() # Création de liste 
print(nevin)
nevin.append("Football") #Ajoutr l'élement football à la liste
print(nevin)

nevin.append(1)
nevin.append(2)
nevin.append(3)
print(nevin)

repas= ["pizza", "jus","glace"]
print(repas)
repas.append(1) # Ajouter l'élement 1 à la liste repas 
print(repas)


# Liste de 0 à 19

listea19 = list(range(20)) #Suite de nombre de 0 à 19 saut de 1 
print(listea19)

3# dexième essaie 

listea19 =list(range(0,20))
print(listea19)

listea19 = list(range(0,50,3))
print(listea19)

longueurliste = len(listea19)
print(longueurliste)


element = listea19[16]
print(element)

elm = listea19[-1] #Trouver une elements de la liste 
print(elm)

listdi = ["Dino", (3)]
print(listdi)

listn = ["pancake"]
print(listn)

megalist = [listn,listdi]
print(megalist)

ele = megalist[1][1]
print(ele)

newlist = [3,2,1]
print(newlist)
newlist.sort()  # Trier des éelements
print(newlist)

listdi.pop(0) 
print(listdi)