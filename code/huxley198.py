# #loop
n = int(input())           # Recebe o número inteiro n

soma_tempo = 0             # Inicializa a soma dos tempos

for i in range(n):         # Loop para receber os tempos
    tempo = int(input())  # Recebe cada tempo
    soma_tempo += tempo     # Adiciona o tempo à soma

print(f"{soma_tempo:.0f}")
