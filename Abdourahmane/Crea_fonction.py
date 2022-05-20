#---- Partie 2 - creation de fonctions

# Fonction pour afficher une carte étudiante
def CarteEtu (nom,prenom,numetu):
    print()
    print("--- Carte étudiante ---")
    print("Nom :", nom)
    print("Prenom :", prenom)
    print("Numéro étudiant :",numetu)
    
# Appel de la fonction
CarteEtu("Bibi", "Blogsberg", 69666)

# Fonction calculant une moyenne sur 5 notes
def moy_5 (n1,n2,n3,n4, n5):
    #--calcul
    Moy = (n1 + n2 + n3 + n4 + n5)/5

    #affichage
    print()
    print("--- Moyenne sur 5 notes ---")
    print("Votre moyenne est de : ", Moy)

# Appel de la fonction
moy_5(7, 8 ,7, 9 ,20)

# Fonction calculant une médiane sur 5 notes
"""
def med_5(n1,n2,n3,n4,n5):

"""