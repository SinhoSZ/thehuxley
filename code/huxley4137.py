figura = input()
tamanho = float(input())

if tamanho <= 0:
        print("Entrada invalida!")
else:
    if figura == "c" or figura == "C":
        area = 3.141 * (tamanho ** 2)
        print(f"{area:.2f}")
        print("Circulo")
    elif figura == "q" or figura == "Q":
        area = tamanho ** 2
        print(f"{area:.2f}")
        print("Quadrado")
    elif figura == "t" or figura == "T":
        area = ((tamanho ** 2) * 1.7) / 4
        print(f"{area:.2f}")
        print("Triangulo equilatero")
    else:
        print("Entrada invalida!")

# Considere raiz de 3 = 1.7 e pi = 3.141