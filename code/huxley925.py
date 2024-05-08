num1 = float(input())
num2 = float(input())
num3 = float(input())

if num1 == num2 and num1 == num3:
    print("Informe o comprimento do primeiro lado do triangulo:")
    print("Informe o comprimento do segundo lado do triangulo:")
    print("Informe o comprimento do terceiro lado do triangulo:")
    print("Os lados informados podem formar um triangulo")
    print("Triangulo Equilatero")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Informe o comprimento do primeiro lado do triangulo:")
    print("Informe o comprimento do segundo lado do triangulo:")
    print("Informe o comprimento do terceiro lado do triangulo:")
    print("Os lados informados podem formar um triangulo")
    print("Triangulo Isosceles")
else:
    print("Informe o comprimento do primeiro lado do triangulo:")
    print("Informe o comprimento do segundo lado do triangulo:")
    print("Informe o comprimento do terceiro lado do triangulo:")
    print("Os lados informados podem formar um triangulo")
    print("Triangulo Escaleno")

