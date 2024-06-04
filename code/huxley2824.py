pessoas = int(input())
lugar = int(input())
quartos = int(input())

if lugar == 1:
    passeio = pessoas * 75
    if quartos == 2:
        preço = passeio + 600
        divisao = preço / pessoas
        print("Digite a quantidade de pessoas:")
        print("Selecione a cidade escolhida: (1 - Pipa e 2 - Fortaleza)")
        print("Digite a quantidade de quartos:")
        print(f"Valor total da viagem: R$ {preço:.2f}")
        print(f"Valor por pessoa: R$ {divisao:.2f}")
    elif quartos == 3:
        preço = passeio + 900
        divisao = preço / pessoas
        print("Digite a quantidade de pessoas:")
        print("Selecione a cidade escolhida: (1 - Pipa e 2 - Fortaleza)")
        print("Digite a quantidade de quartos:")
        print(f"Valor total da viagem: R$ {preço:.2f}")
        print(f"Valor por pessoa: R$ {divisao:.2f}")
elif lugar == 2:
    parque = pessoas * 60
    if quartos == 3:
        preço = parque + 950
        divisao = preço / pessoas
        print("Digite a quantidade de pessoas:")
        print("Selecione a cidade escolhida: (1 - Pipa e 2 - Fortaleza)")
        print("Digite a quantidade de quartos:")
        print(f"Valor total da viagem: R$ {preço:.2f}")
        print(f"Valor por pessoa: R$ {divisao:.2f}")
    elif quartos == 4:
        preço = parque + 1120
        divisao = preço / pessoas
        print("Digite a quantidade de pessoas:")
        print("Selecione a cidade escolhida: (1 - Pipa e 2 - Fortaleza)")
        print("Digite a quantidade de quartos:")
        print(f"Valor total da viagem: R$ {preço:.2f}")
        print(f"Valor por pessoa: R$ {divisao:.2f}")