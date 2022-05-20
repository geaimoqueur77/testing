def CarteEtu( nom, prenom, num) :
    print('-----Carte étudiante-----')
    print('nom :', nom)
    print('prénom', prenom)
    print('Numéro étudiant', num)

    #On definit la fonction moyenne a l'interieur de CarteEtu()
    def Summary():
        i = 0
        notes = list()
        while i <5 : 
            print('Rentrez votre note ', i+1, ' : ')
            notes.append(int(input()))
            i +=1
        j = 0
        somme = 0
        notes.sort()
        while j < 5 :
            somme = somme + notes[j]
            j +=1
        mediane = notes[3]
        moyenne = somme / 5
        return moyenne, mediane
    print('Rentrez vos notes : ')
    

    #On appelle moyenne dans un print, à l'interieur de CarteEtu()
    (a,b) =Summary()
    print('Moyenne de', prenom, ' : ' , a)
    print('Mediane de ', prenom, ' : ', b )


CarteEtu('Muller', 'Lucas', 2201524)

