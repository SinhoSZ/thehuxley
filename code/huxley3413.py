linha = input() # "2 3"
lista = linha.split() # ["2","3"]
a = int(lista[0]) # 2

for index in range(0, a + 1, 2): # vai contar todos os números do 6 ao 19,de 2 em 2
  print(index, end="   ")    # Imprimir os números lado a lado com 3 espaços entre eles