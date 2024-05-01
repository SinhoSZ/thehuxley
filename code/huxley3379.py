idade = input() # "2"
lista = idade.split() # ["2"]

resultado = int(lista[0]) # 2


if resultado >= 18:
    print("Maior de Idade")

elif resultado < 18:
    print("Menor de Idade")

