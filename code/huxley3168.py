linha = input() # "2 3"
lista = linha.split() # ["2","3"]
a = int(lista[0]) # 2
b = int(lista[1]) # 3 
c = int(lista[2])

#  retorna 2 * a, se c > a; caso contrário, retorna 3 * b.

if c > a:
    retorna1 = (2 * a)
    print(retorna1)
else:
    retorna2 = (3 * b)
    print(retorna2)