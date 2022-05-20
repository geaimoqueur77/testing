Nathanael=list() #création d'une liste vide
print(Nathanael)

Nathanael.append("Basket") #ajouter un élément à la liste
print(Nathanael)
Nathanael.append(21)
print(Nathanael)
Courses=["Oeufs","Viande","Pâtes","Légumes"]
print(Courses)
Courses.append("Lait") 
print(Courses)
Stephane=[12,13,15,18]
print(Stephane)

ListMixt=["J'ai",21,"ans"]
print(ListMixt)
ZeA19=list(range(20)) #afficher de 0 à 19
print(ZeA19)
ZeA50_3=list(range(0,50,3)) #0 à 50 en 3 par 3
print(ZeA50_3)
longueurZeA50= len(ZeA50_3) #longueur de la liste
print(longueurZeA50)
LstEl=ZeA50_3[longueurZeA50-1] #dernier élément de la liste
print("Dernier élément ",LstEl)

Dino=["Dinosaure",3]
print(Dino)
Pncks=["Pancakes",32]
print(Pncks)

Megaliste=[Dino,Pncks]
print(Megaliste)
Element=Megaliste[0][1] #2e élément de la première liste
print(Element)

LstChfr=[3,2,1]
LstChfr.sort()
print(LstChfr)

Dino.pop(0) #Suppression d'un élément d'une liste
print(Dino)

