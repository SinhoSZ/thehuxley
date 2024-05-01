linha1 = input() # "2 3"
lista1 = linha1.split() # ["2","3"]
linha2 = input() # "2 3"
lista2 = linha2.split() # ["2","3"]
linha3 = input() # "2 3"
lista3 = linha3.split() # ["2","3"]

nota_1 = float(lista2[0]) # 2
nota_2 = float(lista2[0]) # 2
nota_3 = float(lista3[0]) # 2

media = ((nota_1 + nota_2 + nota_3) / 3)
print("Informe a primeira nota:")
print("Informe a segunda nota:")
print("Informe a terceira nota:")

if media >= 7:
    print(f"Aprovado com media {media:.1f}")
elif media >= 5.0 and media < 7.0:
    print(f"Recuperacao com media {media:.1f}")
elif media < 5.0:
    print(f"Reprovado com media {media:.1f}")



# Média de reprovação: < 5.0;