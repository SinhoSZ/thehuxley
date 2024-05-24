linha = input() # "2 3"
lista = linha.split() # ["2","3"]
d = int(lista[0]) # 2
p = int(lista[1]) # 3 
u = int(lista[2]) # 3 
n = int(lista[3]) # 3 

resultado_0 = p - d
calculo = (n + d) + (p - d) + (u - resultado_0)
print(calculo)