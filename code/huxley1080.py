temperatura = input()
valor = float(input())

if temperatura == "C":
    if valor <= -273.15:
        print("Valor de temperatura abaixo do minimo")
    else:
        c_f = (valor * 1.8) + 32  # Celsius para Fahrenheit
        c_k = valor + 273.15      # Celsius para Kelvin
        print(f"{c_f:.2f} F")
        print(f"{c_k:.2f} K")
elif temperatura == "F":
    if valor <= -459.67:
        print("Valor de temperatura abaixo do minimo")
    else:
        f_c = (valor - 32) / 1.8               # Fahrenheit para Celsius
        f_k = ((valor - 32) * (5/9)) + 273.15  # Fahrenheit para Kelvin
        print(f"{f_c:.2f} C")
        print(f"{f_k:.2f} K")
elif temperatura == "K":
    if valor <= 0:
        print("Valor de temperatura abaixo do minimo")
    else:
        k_c = valor - 273.15               # Kelvin para Celsius
        k_f = ((valor - 273.15) * 1.8) + 32  # Kelvin para Fahrenheit
        print(f"{k_c:.2f} C")
        print(f"{k_f:.2f} F")
else:
    print("Escala de temperatura inválida")

# Celsius: t >= -273.15
# Fahrenheit: t >= -459.67
# Kelvin: t >= 0.0
