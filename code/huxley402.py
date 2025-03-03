def EstacaoAno(dia, mes):
    if (mes == 9 and dia >= 21) or (mes > 9 and mes <= 12):
        print("PRIMAVERA")
    elif (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 3):
        print("VERAO")
    elif (mes == 3 and dia >= 21) or (mes > 3 and mes <= 6):
        print("OUTONO")
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes <= 9):
        print("INVERNO")

# Entrada de dados
dia = int(input())
mes = int(input())

# Chamada da função com os parâmetros corretos
EstacaoAno(dia, mes)
