consumo = float(input())

if consumo <= 99:
    soma = 1.35 * consumo
    tarifa = 1.35
elif consumo <= 299:
    soma = 1.55 * consumo
    tarifa = 1.55
elif consumo <= 574:
    calculo = 1.75 * consumo
    soma = calculo + (calculo * 0.10)
    tarifa = 1.75
else:
    calculo = 2.15 * consumo
    soma = calculo + (calculo * 0.10)
    tarifa = 2.15

# Garantir que o valor mínimo da conta seja R$ 35
if soma < 35:
    soma = 35

print(f"{soma:.2f}")
print(f"{tarifa:.2f}")
