peso = float(input())
altura = float(input())

imc = peso / altura ** 2
if imc < 18 or imc > 25:
    print(f"{imc:.2f}")
    print("atencao")
else:
    print(f"{imc:.2f}")
    print("normal")
