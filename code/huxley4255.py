linha = input() # "2"
lista = linha.split() # ["2"]
linha2 = input() # "3"
lista2 = linha2.split() # ["3"]

a = int(lista[0]) # 2
b = int(lista2[0]) # 3 


if a == b:
    print(a, end="\n")
    print(b, end="\n")
elif a > b:
    print(b, end="\n")
    print(a, end="\n")
elif a < b:
    print(a, end="\n")
    print(b, end="\n")
    


