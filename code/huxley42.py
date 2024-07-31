idade = int(input())

if idade <= 15:
    print("nao eleitor")
elif idade >= 18 and idade <= 65:
    print("eleitor obrigatorio")
else:
    print("eleitor facultativo")