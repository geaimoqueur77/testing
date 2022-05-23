intervalle=list(range(1,16))

def multiple(intervalle):

    for i in intervalle:
        if i % 3 == 0 and i % 5 != 0:
            print ("fizz")
        if i % 5 == 0 and i % 3 != 0:
           print ("buzz")
        if i % 3 == 0 and i % 5 == 0:
             print ("fizzbuzz")
        else:
            print(i)




print("la sortie est :", multiple(intervalle))