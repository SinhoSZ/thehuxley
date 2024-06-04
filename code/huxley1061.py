r1 = float(input())
r2 = float(input())

pi = 3.14
calculo = pi * (r1 ** 2)
calculo2 = pi * (r2 ** 2)


if calculo == calculo2:
    print("Iguais")
elif calculo > calculo2:
    print("Primeiro circulo")
else:
    print("Segundo circulo")