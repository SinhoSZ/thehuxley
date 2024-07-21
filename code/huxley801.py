linha = input() # Exemplo de entrada: "2"
lista = linha.split() # ["2"]

# Converte os elementos da lista para floateiros
a = float(lista[0]) 
b = float(lista[1]) 
c = float(lista[2]) 
d = float(lista[3]) 

peso1 = 1
peso2 = 2
peso3 = 3
peso4 = 4

soma_peso = (peso1 + peso2 + peso3 + peso4)
nota = (((a * peso1) + (b *peso2) + (c * peso3) + (d * peso4)) / soma_peso)

if nota >= 9:
    print("aprovado com louvor")
elif nota >= 7:
    print("aprovado")
elif nota < 3:
    print("reprovado")
else:
    print("prova final")
