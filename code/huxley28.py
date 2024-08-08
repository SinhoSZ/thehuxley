numero = int(input())

# Inverte o número convertendo-o para string e removendo os zeros à esquerda
numero_invertido = str(numero)[::-1].lstrip('0')

print(numero_invertido)
