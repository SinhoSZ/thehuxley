linha = input() # Exemplo de entrada: "2"
lista = linha.split() # ["2"]

a = int(lista[0]) 
b = int(lista[1])
c = int(lista[2])

resultado = max(a, b, c)
print(resultado)