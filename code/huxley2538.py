num = int(input())

a = 0.30
b = 0.25

if num < 12:
    soma = (num * a)
    print("Digite a quantidade de macas:")
    print(f"Valor total: R$ {soma:.0f}")
elif num >= 12:
    soma1 = (num * b)
    print("Digite a quantidade de macas:")
    print(f"Valor total: R$ {soma1:.0f}")