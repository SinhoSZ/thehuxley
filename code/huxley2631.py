alice = int(input())
beto = int(input())
clara = int(input())

if alice not in (0, 1) or beto not in (0, 1) or clara not in (0, 1): # Verifica se todos os valores são 0 ou 1
    print("Digite o valor de Alice:")
    print("Digite o valor de Beto:")
    print("Digite o valor de Clara:")
    print("Algum valor digitado e diferente de 0 ou 1.")
else:
    if alice == beto and beto == clara:
        print("Digite o valor de Alice:")
        print("Digite o valor de Beto:")
        print("Digite o valor de Clara:")
        print("Nao houve vencedor.")
    elif alice == beto and beto != clara:
        print("Digite o valor de Alice:")
        print("Digite o valor de Beto:")
        print("Digite o valor de Clara:")
        print("O vencedor e Clara.")
    elif alice == clara and clara != beto:
        print("Digite o valor de Alice:")
        print("Digite o valor de Beto:")
        print("Digite o valor de Clara:")
        print("O vencedor e Beto.")
    elif beto == clara and clara != alice:
      print("Digite o valor de Alice:")
      print("Digite o valor de Beto:")
      print("Digite o valor de Clara:")
      print("O vencedor e Alice.")