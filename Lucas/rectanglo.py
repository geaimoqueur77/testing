def carre (dim) : 
    print(' ' + '__'* dim +'  ' )
    for j in range(dim):
        chain = "|"
        for i in range(dim) : 
            chain += '**'
            if i == dim - 1 :
                chain += '|'
        print(chain)
        chain = ''
    print(' ' + '--'* dim +'  ' )
    
def rectangle (dim) : 
    print(' ' + '__'* dim +'  ' )
    for j in range(dim*2):
        chain = "|"
        for i in range(dim) : 
            chain += '**'
            if i == dim - 1 :
                chain += '|'
        print(chain)
        chain = ''
    print(' ' + '--'* dim +'  ' ) 

a = int(input())
carre(a)
rectangle(a)


    
