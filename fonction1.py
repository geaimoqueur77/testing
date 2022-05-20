# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:46:51 2022

@author: HP
"""

#CREATION DE FONCTION 

def Etudiant(nom,prenom,numetu):
    
    print("-- Carte etudiante --")
    print("Nom:",nom)
    print("Prenom:",prenom)
    print("Numero etudiant:",numetu)
Etudiant("Dieng","Ndeye Fatou",53421)

def noteetu(n1,n2,n3):
    
    moyenne= (n1+n2+n3)/3
    print("La moyenne est de :",moyenne)
noteetu(10,15,12)