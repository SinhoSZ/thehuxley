a = input().lower() # Converte para minúsculas
b = input().lower() # Converte para minúsculas

if a in ("s", "n") and b in ("s", "n"):  # Verifica se a entrada está correta
    if a == "s" or b == "s":  # Se o cliente é estudante ou idoso
        print("Cliente e estudante? (s ou n)")
        print("Cliente e idoso? (s ou n)")
        print("Meia-entrada. Valor a ser pago: R$10,00.")
    else:  # Se o cliente não é estudante nem idoso
        print("Cliente e estudante? (s ou n)")
        print("Cliente e idoso? (s ou n)")
        print("Entrada completa. Valor a ser pago: R$20,00.")
else:
    print("Cliente e estudante? (s ou n)")
    print("Cliente e idoso? (s ou n)")
    print("Entrada deve ser apenas pelas letras s ou n.")