def chiff(nombre, chiffres):
        resultat=""
        for i in nombre:
            if i not in chiffres:
                resultat +=i #variable contient les numbres qui ne sont pas dans la liste chiffres
        return resultat


nb = "123456"
chiffres= ["1","2"]
print(chiff(nb, chiffres))