entrada = input()

if entrada == "c":
    calcular = input()
    if calcular == "v":
        raio = float(input())
        altura = float(input())
        volume = ((3.1415 * (raio**2) * altura))
        print(f"O volume do cilindro de raio {raio:.2f} e altura {altura:.2f} eh:")
        print(f"{volume:.2f}")
    elif calcular == "a":
        raio = float(input())
        altura = float(input())
        area = (2 * 3.1415 * raio) * (raio + altura)
        print(f"A area do cilindro de raio {raio:.2f} e altura {altura:.2f} eh:")
        print(f"{area:.2f}")
    else:
        print("Entrada invalida! Entre com 'a' (area) ou 'v' (volume).")
elif entrada == "e":
    calcular = input()
    if calcular == "v":
        raio = float(input())
        volume = (((4 / 3) * 3.1415) * raio**3)
        print(f"O volume da esfera de raio {raio:.2f} eh:")
        print(f"{volume:.2f}")
    elif calcular == "a":
        raio = float(input())
        area = ((4 * 3.1415) * raio**2)
        print(f"A area da esfera de raio {raio:.2f} eh:")
        print(f"{area:.2f}")
    else:
        print("Entrada invalida! Entre com 'a' (area) ou 'v' (volume).")
else:
    print("Entrada invalida! Voce deve usar 'c' (cilindro) ou 'e' (esfera).")