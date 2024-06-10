def maior(a, l, p):
    return max(a, l, p)

linha = input() # Exemplo de entrada: "2"
lista = linha.split() # ["2"]
h = int(input())

a = int(lista[0]) 
l = int(lista[1]) 
p = int(lista[2]) 

resultado = maior(a, l, p)

soma = h * resultado
print(soma)