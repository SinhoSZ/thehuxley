num = float(input())

if num >= 20:
    porcentagem = num * 0.30
    soma = num + porcentagem
    print("Digite o valor de compra do produto:")
    print(f"O produto deve ser vendido a R$ {soma:.2f}")
else:
    porcentagem = num * 0.45
    soma = num + porcentagem
    print("Digite o valor de compra do produto:")
    print(f"O produto deve ser vendido a R$ {soma:.2f}")