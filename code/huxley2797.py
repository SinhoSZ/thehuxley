linha = input() # Exemplo de entrada: "2"
lista = linha.split() # ["2"]

# Converte os elementos da lista para inteiros
alice = int(lista[0]) 
beto = int(lista[1]) 
clara = int(lista[2]) 

if alice not in (0, 1) or beto not in (0, 1) or clara not in (0, 1): # Verifica se todos os valores são 0 ou 1
    print("*")
else:
    if alice == beto and beto == clara:
        print("*")
    elif alice == beto and beto != clara:
        print("C")
    elif alice == clara and clara != beto:
        print("B")
    elif beto == clara and clara != alice:
      print("A")