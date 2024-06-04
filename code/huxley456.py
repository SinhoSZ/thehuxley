pessoas = int(input())
lugar = input().upper()
quartos = int(input())

if lugar == "pipa" or lugar == "PIPA":
    passeio = pessoas * 75
    if quartos == 2:
        preço = passeio + 600
        divisao = preço / pessoas
        print(f"{preço:.2f}")
        print(f"{divisao:.2f}")
    elif quartos == 3:
        preço = passeio + 900
        divisao = preço / pessoas
        print(f"{preço:.2f}")
        print(f"{divisao:.2f}")
elif lugar == "fortaleza" or lugar == "FORTALEZA":
    parque = pessoas * 60
    if quartos == 3:
        preço = parque + 950
        divisao = preço / pessoas
        print(f"{preço:.2f}")
        print(f"{divisao:.2f}")
    elif quartos == 4:
        preço = parque + 1120
        divisao = preço / pessoas
        print(f"{preço:.2f}")
        print(f"{divisao:.2f}")