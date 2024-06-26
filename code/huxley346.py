# Função para encontrar todos os divisores de um número inteiro positivo
def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

numero = int(input())

# Verificar se o número é positivo
if numero > 0:
    divisores = encontrar_divisores(numero)
    for divisor in sorted(divisores):
        print(divisor)