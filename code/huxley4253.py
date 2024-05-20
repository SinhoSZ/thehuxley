nome = input()

if nome == "retangulo":
    base = int(input())
    altura = int(input())
    calculo = base * altura
    print(f"{calculo:.2f}")
elif nome == "triangulo":
    base = int(input())
    altura = int(input())
    calculo = (base * altura) / 2
    print(f"{calculo:.2f}")
elif nome == "trapezio":
    basemaior = int(input())
    basemenor = int(input())
    altura = int(input())
    calcuclo = ((basemaior + basemenor)*altura)/2
    print(f"{calcuclo:.2f}")
elif nome == "circulo":
    raio = float(input())
    calculo = (3.1415 * (raio**2))
    print(f"{calculo:.2f}")
else:
    print("Figura invalida.")