num1 = float(input())
num2 = float(input())
num3 = float(input())

if num1 == num2 and num1 == num3:
    print("Digite o comprimento do lado A:")
    print("Digite o comprimento do lado B:")
    print("Digite o comprimento do lado C:")
    print("Este e um triangulo equilatero.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Digite o comprimento do lado A:")
    print("Digite o comprimento do lado B:")
    print("Digite o comprimento do lado C:")
    print("Este e um triangulo isosceles.")
else:
    print("Digite o comprimento do lado A:")
    print("Digite o comprimento do lado B:")
    print("Digite o comprimento do lado C:")
    print("Este e um triangulo escaleno.")