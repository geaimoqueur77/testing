import turtle 
x = turtle.Turtle() 


def squarre(): 
    x.fillcolor('orange')   
    x.begin_fill() 
    x.left(0) 
    x.forward(150) 
    x.left(90) 
    x.forward(150)
    x.left(90) 
    x.forward(150)
    x.left(90) 
    x.forward(150)
    x.end_fill() 

def txt():  
    x.up() 
    x.setpos(-68, 95)    
    x.down()    
    x.color('red')    
    x.write("Victoire", font=( 
      "Arial", 12, "bold"))   


squarre()  
txt() 
x.ht()

