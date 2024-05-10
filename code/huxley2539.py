lados = int(input()) 
medida = int(input())

import math

if lados <= 2:
    print("Digite o numero de lados:")
    print("Digite a medida do lado em cm:")
    print("NAO E UM POLIGONO")
elif lados >= 6:
    print("Digite o numero de lados:")
    print("Digite a medida do lado em cm:")
    print("POLIGONO NAO IDENTIFICADO")
elif lados == 5:
    print("Digite o numero de lados:")
    print("Digite a medida do lado em cm:")
    print("PENTAGONO")
elif lados == 4:
    calculo = medida * medida
    print("Digite o numero de lados:")
    print("Digite a medida do lado em cm:")
    print("QUADRADO")
    print(f"A area do poligono e: {calculo} cm2")
elif lados == 3:
    calculo = (((medida ** 2) * math.sqrt(3)) / 4 )
    print("Digite o numero de lados:")
    print("Digite a medida do lado em cm:")
    print("TRIANGULO")
    print(f"A area do poligono e: {calculo:.4f} cm2")
