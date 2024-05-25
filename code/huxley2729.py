def menor_ou_maior(x):
    if x >= 0:
        return 1
    else:
        return 0
    
x = int(input())

resposta = menor_ou_maior(x)
if resposta == 1:
    print("nao menor")
elif resposta == 0:
    print("menor")
