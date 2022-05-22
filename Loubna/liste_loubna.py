from subprocess import list2cmdline


loubna = list()
print(loubna)
loubna.append("Jouer du piano")#ajouter un élément à la liste
loubna.append("Danse")#ajouter un élément à la liste
loubna.append(4)#ajouter un élément à la liste
print(loubna)



repas=["gateau", "pizza", "poisson"]
note=[20,17]
print(repas)
print(note)

age=["age", 23]
print(age)

r1=list(range(1,20))
print(r1)


r2=list(range(3 ,50 ,3))
print(r2)

longeur=len(r2)#connaitre la longeur d'une liste
print(longeur)


index=r2[-1]#connaitre le dernier élément de la liste

print(index)

print(r2[15])


list1=["dinasaure", 3]
print(list1)
list2=["pizza"]
print(list2cmdline)

megaList=[list1,list2]
print(megaList)

Element=megaList[0][1]#connaitre la deuxieme élément de la premiere liste
print(Element)

list3=[3,2,1]
print(list3)
list3.sort()
print(list3)

list1.pop(0)#pour mettre dans l'ordre les éléments de la liste
print(list1)



