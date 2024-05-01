poluicao = float(input())

if poluicao >= 0.26 and poluicao <= 0.30:
    print("Grupo 1")
elif poluicao >= 0.31 and poluicao <= 0.40:
    print("Grupo 1")
    print("Grupo 2")
elif poluicao >= 0.41:
    print("Grupo 1")
    print("Grupo 2")
    print("Grupo 3")



# O índice de poluição aceitável varia de 0,05 até 0,25.
# Se o índice foge desse intervalo até 0,3, as indústrias do 1º grupo são intimadas a suspenderem suas atividades
# se o índice crescer até 0,4 as industrias do 1º e 2º grupo são intimadas a suspenderem suas atividades
# se superar 0,4, todos os grupos devem ser notificados a paralisarem suas atividades.