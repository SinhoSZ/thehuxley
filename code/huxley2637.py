# Obs
partida_1 = int(input())
partida_2 = int(input())
partida_3 = int(input())
partida_4 = int(input())
partida_5 = int(input())
partida_6 = int(input())

if partida_1 >= 0 and partida_2 >= 0 and partida_3 >= 0 and partida_4 >= 0 and partida_5 >= 0 and partida_6 >= 0:
    soma = (partida_6 + partida_5 + partida_4 + partida_3 + partida_2 + partida_1)
    if soma >= 100:
        print("Digite pontuacao da partida 1:")
        print("Digite pontuacao da partida 2:")
        print("Digite pontuacao da partida 3:")
        print("Digite pontuacao da partida 4:")
        print("Digite pontuacao da partida 5:")
        print("Digite pontuacao da partida 6:")
        print(f"Total de pontos: {soma}. O competidor esta classificado.")
    else:
        print("Digite pontuacao da partida 1:")
        print("Digite pontuacao da partida 2:")
        print("Digite pontuacao da partida 3:")
        print("Digite pontuacao da partida 4:")
        print("Digite pontuacao da partida 5:")
        print("Digite pontuacao da partida 6:")
        print(f"Total de pontos: {soma}. O competidor esta desclassificado.")
else:
    print("Digite pontuacao da partida 1:")
    print("Digite pontuacao da partida 2:")
    print("Digite pontuacao da partida 3:")
    print("Digite pontuacao da partida 4:")
    print("Digite pontuacao da partida 5:")
    print("Digite pontuacao da partida 6:")
    print("Valores negativos nao sao permitidos.")