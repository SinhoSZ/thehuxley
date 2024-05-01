linha = input() # Exemplo de entrada: "2"
lista = linha.split() # ["2"]
linha1 = input() # Exemplo de entrada: "3"
lista1 = linha1.split() # ["3"]
linha2 = input() # Exemplo de entrada: "4"
lista2 = linha2.split() # ["4"]

# Converte os elementos da lista para inteiros
a = int(lista[0]) 
b = int(lista1[0]) 
c = int(lista2[0]) 

# Ordenar os números
ordenados = sorted([a, b, c])

# Imprimir os números em ordem crescente
for numero in ordenados:
    print(numero)