linha1 = input() # "2 3"
lista1 = linha1.split() # ["2","3"]

a = float(lista1[0]) 
b = float(lista1[1]) 
c = float(lista1[2]) 
d = float(lista1[3]) 
e = float(lista1[4]) 

soma = ((a + b + c)/(d + e))
resultado = (f"{soma:.2f}")
print(resultado)
