sexo = int(input())    # Recebendo as entradas do usuário
altura = float(input())

# Verifica se os valores são negativos
if sexo < 0 or sexo >= 3:
    print("Digite o sexo: (0 - M e 1 - F)")
    print("Digite a altura em metros:")
    print("O sexo informado e invalido")
elif altura <= 0:
    print("Digite o sexo: (0 - M e 1 - F)")
    print("Digite a altura em metros:")
    print("Altura invalida")
elif sexo == 0:
    homem = ((72.7 * altura) - 58)
    print("Digite o sexo: (0 - M e 1 - F)")
    print("Digite a altura em metros:")
    print(f"Peso ideal: {homem:.1f} kg")
elif sexo == 1:
    Mulheres = ((62.1 * altura) - 44.7)
    print("Digite o sexo: (0 - M e 1 - F)")
    print("Digite a altura em metros:")
    print(f"Peso ideal: {Mulheres:.1f} kg")
