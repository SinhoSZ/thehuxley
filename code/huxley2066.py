n = int(input())           # Recebe o número inteiro n

soma = 0             # Inicializa a soma da n

for i in range(n):         # Loop para receber as n
    nota = float(input())  # Recebe cada n
    soma += nota     # Adiciona a nota à soma


print(f"{soma:.0f}")          # Exibe a média das notas