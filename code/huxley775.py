massa = float(input())
altura = float(input())

imc = (massa / (altura**2))

if imc <= 18.5:
    print(f"{imc:.2f} MAGREZA")
elif imc <= 24.9:
    print(f"{imc:.2f} SAUDAVEL")
elif imc <= 29.9:
    print(f"{imc:.2f} SOBREPESO")
elif imc >= 30:
    print(f"{imc:.2f} OBESIDADE")