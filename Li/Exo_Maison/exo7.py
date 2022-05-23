# si le nombre est divisible par 3 : on affiche Fizz ;
# si le nombre est divisible par 5 : on affiche Buzz ;
# si le nombre est divisible par 3 et par 5 : on affiche Fizzbuzz ;
# sinon on affiche le nombre.

def fizzbuzz():
    var=1
    while var ==1:
        num1 = float(input('choisir un nombre1 (entre 1~20) : '))
        if num1>=1 and num1<=20:
            print("si ",num1," est divisible par 3 ou 5 ?")
            r = num1 % 3
            t = num1 % 5
            print ("%s / 3 = %s"%(num1,num1/3))
            print ("%s / 5 = %s"%(num1,num1/5))

            if r == 0 and t!= 0:
                print("Fizz")
            if t == 0 and r!=0:
                print("Buzz")
            if t == 0 and r == 0:
                print("FizzBuzz")   
fizzbuzz()

            