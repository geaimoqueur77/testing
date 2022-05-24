import turtle 
x = turtle.Turtle() 

def affiche():  
    x.up() 
    x.setpos(-68, 95)    
    x.down()    
    x.color('red')    
    x.write("BIEN JOUE", font=( 
      "Arial", 60, "bold"))  

def carremorray(): 
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
    affiche()

 

carremorray()  
