# Entradas de dados
situacao_ensino_medio = input()
encceja_2017 = input() 
nota_encceja = int(input())
estudou = input()
renda_pessoal = float(input())

# Verificação das condições para isenção
if situacao_ensino_medio == "CVC":
    if estudou == "PUB":
        print("Voce terah direito a isencao")
    else:
         print("Infelizmente voce nao tem direito a isencao")
    

elif situacao_ensino_medio == "CLD":
    if encceja_2017 == "s" and nota_encceja >= 400:
        print("Voce terah direito a isencao")
    elif (estudou == "PUB" or estudou == "PPB") or (estudou == "PCB" and renda_pessoal <= 1431):
        print("Voce terah direito a isencao")
    else:
        print("Infelizmente voce nao tem direito a isencao")

elif situacao_ensino_medio == "CSC":
    if encceja_2017 == "s" and nota_encceja >= 400:
        print("Voce terah direito a isencao")
    elif estudou == "PUB" or estudou == "PPB":
        print("Voce terah direito a isencao")
    else:
        print("Infelizmente voce nao tem direito a isencao")

elif situacao_ensino_medio == "NCC":
    if encceja_2017 == "s" and nota_encceja >= 400:
        print("Voce terah direito a isencao")
    elif estudou == "PUB" or estudou == "PPB":
        print("Voce terah direito a isencao")
    else:
        print("Infelizmente voce nao tem direito a isencao")

else:
    print("Informacao sobre ensino medio invalida")