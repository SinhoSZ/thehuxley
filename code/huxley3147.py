def maior(numero):
    if a > b:
        print(f"{b} {a}")
    elif a < b:
        print(f"{a} {b}")
    
numero = input()
lista = numero.split()
a = int(lista[0]) 
b = int(lista[1]) 

resultado = maior(numero)

