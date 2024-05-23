n = int(input())  # Recebe o número inteiro n

soma = 0  # Inicializa a variável soma
tem_negativo = False  # Inicializa a variável para verificar se há números negativos

for i in range(n):  # Loop para receber os números
    num = int(input())  # Lê o número
    if num < 0:
        tem_negativo = True  # Define a variável como True se encontrar um número negativo
    soma += num  # Adiciona o número diretamente à variável soma

# Imprime a soma final
print(f"{soma}")