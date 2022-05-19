min = int(input())

max = int(input())

def fizzbuzz(ent1, ent2) : 
    a = ent1
    while a <= ent2 : 
        if (a%3 == 0) and (a%5 == 0) :
            print("fizzbuzz")
        else :
            if a%3 == 0 :
                print("fizz")    
            elif a%5 == 0 :
                print("buzz")
        a +=1

        

fizzbuzz(min, max)       