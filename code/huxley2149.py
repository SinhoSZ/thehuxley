nacionalidade = input()
ocupacao = input()
quantidade_armas = int(input())
calibre = int(input())

if nacionalidade == "B": # (B)rasileiro
    if ocupacao == "M": # (M)ilitar
        print("Liberado")
    elif ocupacao == "T": # (M)ilitar
        if quantidade_armas <= 1 and calibre <= 22:
            print("Liberado")
        else:
            print("Barrado") 
    elif ocupacao == "C": # (C)aminhoneiro
        if quantidade_armas <= 2 and calibre <= 38:
            print("Liberado")
        else:
            print("Barrado")
    elif ocupacao == "O": #(O)utro
        if quantidade_armas <= 1 and calibre <= 22:
            print("Liberado")
        else:
            print("Barrado") 

elif nacionalidade == "E": #(E)strangeiro
    if quantidade_armas == 0:
        print("Liberado")
    else:
        print("Barrado")