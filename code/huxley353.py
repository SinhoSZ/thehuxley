peso = int(input())
altura = float(input())

IMC = (peso / (altura * altura))

if IMC < 17:
    print("muito abaixo do peso")
elif IMC >= 17 and IMC <= 18.49:
    print("abaixo do peso ")
elif IMC >= 18.5 and IMC <= 24.99:
    print("peso normal")
elif IMC >= 25 and IMC <= 29.99:
    print("acima do peso")
elif IMC >= 30 and IMC <= 34.99:
    print("obesidade")
elif IMC >= 35 and IMC <= 39.99:
    print("obesidade severa")
else:
    print("obesidade morbida")
