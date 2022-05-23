def CarteEtu( nom, prenom, num) :
    print('-----Carte étudiante-----')
    print('nom :', nom)
    print('prénom', prenom)
    print('Numéro étudiant', num)

    #On definit la fonction moyenne a l'interieur de CarteEtu()
    def Summary():
        print('Combien de notes ? ')
        cmb = int(input())
        i = 0
        notes = list()
        somme = 0
        print('Rentrez vos notes : ')
        while i <cmb : 
            print('Rentrez votre note ', i+1, ' : ')
            notes.append(int(input()))
            somme = somme + notes[i]
            i +=1
        notes.sort()
        mediane = notes[cmb // 2]
        moyenne = somme / cmb
        return moyenne, mediane
    
    

    #On appelle moyenne dans un print, à l'interieur de CarteEtu()
    (a,b) =Summary()
    print('Moyenne de', prenom, ' : ' , a)
    print('Mediane de ', prenom, ' : ', b )


CarteEtu('Muller', 'Lucas', 2201524)

