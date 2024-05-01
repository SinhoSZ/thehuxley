linha = input() # "2 3"
lista = linha.split() # ["2","3"]
a = int(lista[0]) # 2
b = int(lista[1]) # 3 

if a == b:
    print(a,b)
elif a > b:
    print(b,a)
elif a < b:
    print(a,b)
    