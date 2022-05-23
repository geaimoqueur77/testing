#j'ai du un peu de mal avec celui là, en me documentant je tombe sur des programmes déjà faits mais petite galère à le faire seul

def factorielle(x,y):
    n = x
    for i in range (x,y):
        n = i * (n - 1)
    

print(factorielle(5,20))