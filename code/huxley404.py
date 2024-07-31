nota = float(input())
falta = int(input())

if falta > 10:
    print("REPROVADO POR FALTAS")
elif nota < 7:
    print("REPROVADO")
elif nota >= 7 and nota <= 9.4:
    if falta < 11:
        print("APROVADO")
elif nota >= 9.5:
    if falta < 11: 
        print("APROVADO COM LOUVOR")