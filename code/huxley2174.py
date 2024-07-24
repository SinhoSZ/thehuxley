linha = input() # Exemplo de entrada: "4"
lista = linha.split() # ["4"]
# Converte os elementos da lista para inteiros
a = float(lista[0]) 
b = float(lista[1])

valor_agua = ((a * 1000) * b)
valor_esgoto = (valor_agua * 0.8)
total = valor_agua + valor_esgoto
print(f"{valor_agua:.2f}")
print(f"{valor_esgoto:.2f}")
print(f"{total:.2f}")