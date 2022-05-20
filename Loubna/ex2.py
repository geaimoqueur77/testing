def filtrer(mot, lettres):
        var = " "
        for lettre in mot:
            if lettre not in lettres:
                var =var+lettre
        return var


mot = "loubna"
lettres = ["e", "i", "a", "y", "u", "o"]
print(filtrer(mot, lettres))