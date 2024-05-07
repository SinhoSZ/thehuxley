def encontrar_maior(a, b, c, d):
    # Encontra o maior entre os quatro números
    return max(a, b, c, d)

# Solicita ao usuário que insira os quatro números
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# Chama a função para encontrar o maior número e imprime o resultado
maior_numero = encontrar_maior(num1, num2, num3, num4)
print(f"{maior_numero:.2f}")