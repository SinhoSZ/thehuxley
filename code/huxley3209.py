# #loop
n = int(input())           # Recebe o número inteiro n
resultados = [] # lista para armazenar os resultados

for i in range(n):         # Loop para receber as quantidades
    linha = input()  # Recebe cada tempo
    lista = linha.split()
    a = int(lista[0]) 
    b = int(lista[1]) 
    c = int(lista[2])
    calculo = (a * b)
    resultado = calculo % c
    resultados.append(resultado) # adiciona o resultado à lista

# imprime todos os resultados
for resultado in resultados:
    print(f"{resultado}")
 
