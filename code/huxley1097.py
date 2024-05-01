sexo = input()
h = float(input())

Homens = (72.7 * h) - 58
Mulheres = ((62.1 * h) - 44.7)

if h <= 0:
     print("Altura invalida.")
else:
    if sexo == "f":
       print(f"{Mulheres:.2f}")
    elif sexo == "m":
       print(f"{Homens:.2f}")
    else:
       print("O sexo informado eh invalido.")
