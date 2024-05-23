num = int(input())

if num == 1:
    valor = input() # Exemplo de entrada: "2"
    lista = valor.split() # ["2"]
    a = int(lista[0]) 
    b = int(lista[1])
    soma = a+b
    print(f"{soma:.2f}") 
elif num == 2:
    valor = int(input())
    import math
    raiz_quadrada = math.sqrt(valor)
    print(f"{raiz_quadrada:.2f}")
else:
    print("Opção inválida!")
