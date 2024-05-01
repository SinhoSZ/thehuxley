n = int(input())           # Recebe o número inteiro n

soma_notas = 0             # Inicializa a soma das notas

for i in range(n):         # Loop para receber as notas
    nota = float(input())  # Recebe cada nota
    soma_notas += nota     # Adiciona a nota à soma

media = soma_notas / n     # Calcula a média das notas

print(f"{media:.2f}")          # Exibe a média das notas