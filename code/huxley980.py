linha = input() # "2"
lista = linha.split() # ["2"]

a = float(lista[0]) # 2

# aumento de 30% < 1000
# aumento de 10% 1000 > 2000
# < 2000 não recebe

if a <= 999:
    calculo_aumento_1 = (a * 0.30)
    aumento_1 = (a + calculo_aumento_1)
    print(f"{aumento_1:.2f}")

elif a >= 1000 and a <= 1999:
    calculo_aumento_2 = (a * 0.10)
    aumento_2 = (a + calculo_aumento_2)
    print(f"{aumento_2:.2f}")

elif a >= 2000:
    print(f"{a:.2f}")
    


