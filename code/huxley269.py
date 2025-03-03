def meses(mes):
    meses_ano = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    
    # Verifica se o mês está no intervalo de 1 a 12
    if 1 <= mes <= 12:
        print(meses_ano[mes - 1])
    else:
        print("invalido")

mes = int(input())

meses(mes)
