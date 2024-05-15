num1 = float(input())
num2 = float(input())
num3 = int(input())

if num3 == 1: # soma
    calculo = num1 + num2
    print(f"{calculo:.3f}")
elif num3 == 2: # subtração
    calculo = num1 - num2
    print(f"{calculo:.3f}")
elif num3 == 3: # multiplicação
    calculo = num1 * num2
    print(f"{calculo:.3f}")
elif num3 == 4: # divisão
    calculo = num1 / num2
    print(f"{calculo:.3f}")