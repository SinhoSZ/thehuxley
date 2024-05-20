Base = int(input())
expoente = int(input())

# Inicializa o resultado como 1 (a identidade multiplicativa)
resultado = 1

# Usa uma estrutura de repetição para multiplicar a base
for _ in range(expoente):
    resultado *= Base

print("Informe a base:")
print("Informe o expoente:")
print(f"Resultado: {resultado}")