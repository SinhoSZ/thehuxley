numero = int(input())  # Solicita ao usuário para inserir um número inteiro

fatorial = 1    # Inicializa o fatorial como 1

# Calcula o fatorial
for i in range(1, numero + 1): 
    fatorial *= i

# Exibe o resultado
print(f"{fatorial}")