lama=list()
print(lama)
lama.append("course à pied")
print(lama)
lama.append(3)
print(lama)

repas=["gateau", "pizza"]
print(repas)


notes=[18, 17]
print(notes)

mixte=["g", 23 ]
print(mixte)

listrange=list(range(20))
print (listrange)

listrange2=list(range(1, 20))
print (listrange2)

listrange3=list(range(0, 50, 3))
print (listrange3)


logeurrange3=len(listrange3)
print(logeurrange3)

index1= listrange3[16]  #1er façon
print(index1)

index2=listrange3[logeurrange3-1]  #2ieme façon
print(index2)

index3=listrange3[-1] #3ieme façon
print(index3)

list1=["dinaseure", 3]
print(list1)

list2=["paincake"]
print(list2)

megaliste=[list1,list2] #liste mixte avec list1 et liste 2 
print(megaliste)

element=megaliste[0][1] #recuperer le 2ime element de la 1ere liste, le 1er indice pour la liste et 2ieme indice pour l'element
print(element)

liste_a=[3, 2, 1]
print(liste_a)
liste_a.sort() #ordonner la liste 
print(liste_a)


list1.pop(0)
print(list1)

