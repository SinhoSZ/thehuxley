def numero_maior(a, b):
    if a > b:
        print(f"{a:.1f}")
    elif b > a:
        print(f"{b:.1f}")
    else:
        print("São iguais")

a = float(input())
b = float(input())

numero_maior(a, b)