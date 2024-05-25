numero = input()
lista = numero.split()

a = float(lista[0]) 
b = float(lista[1]) 
c = float(lista[2]) 

triangulo = (a * c) / 2 #a área do triangulo retângulo que tem A por base e C por altura. 
circulo = 3.14159 * (c**2) # a área do círculo de raio C. (pi = 3.14159)  π r²
trapezio = ((a + b)* c) / 2 # a área do trapézio que tem A e B por bases e c por altura. A=(a+b)h/2.
quadrado = b * b # a área do quadrado que tem lado B. 
retangulo = a * b # a área do retângulo que tem lados A e B. A=b⋅h

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")