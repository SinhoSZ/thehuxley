num = input() # Exemplo de entrada: "2"
lista = num.split() # ["2"]

r = float(lista[0]) 
h = float(lista[1])

formula = ((3.1415 * (r**2)) * h)
print(f"{formula:.2f}")