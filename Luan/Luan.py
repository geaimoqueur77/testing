from numpy import sort


Luan = list()
print(Luan)

Luan.append(1)
print(Luan)

lmots = ["Jus d'orange", "tomates cerises"]
#Notes Stéphane
lnombre = [17,20,12]
print(lnombre)


lmixte = ["j'ai ", 20, " ans"]
print(lmixte)

lrange =range(20)
for i in lrange:
    print(i)

tey = list(range(20))
print(tey)

toma = list(range(0,51,3))
print(toma)

print(len(toma))

dernier = toma[len(toma) - 1]
print(dernier)
print(toma[-1])

bigbang = ["dino", 3]
orange = ["jus d'orange"]

megaliste = [bigbang, orange]
print(megaliste)


#megaliste[n. liste][element]
el = megaliste[0][1]

print(el)

#print(globals())

a = [3,2,1]
print(a)
print(a[-1])

print(sort(a))
print(sort(a)[-1])

b = ["cc","bb","c", ""]
print(b)

print(sort(b))

bigbang.pop(0)
print(bigbang)