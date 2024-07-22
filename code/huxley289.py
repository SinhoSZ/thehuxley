linha = input() # Exemplo de entrada: "4"
lista = linha.split() # ["4"]

altura = int(lista[0]) 
idade = int(lista[1]) 

if altura >= 150 and idade >= 12:
    if altura >= 140 and idade >= 14:
        if altura >= 170 or idade >= 16:
            print("3")
        else:
            print("2")
    else:
        if altura >= 170 or idade >= 16:
            print("2")
        else:
            print("1")
else:
    if altura >= 140 and idade >= 14:
        if altura >= 170 or idade >= 16:
            print("2")
        else:
            print("1")
    else:
        if altura >= 170 or idade >= 16:
            print("1")
        else:
            print("0")