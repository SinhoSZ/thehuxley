x = int(input()) # triangulo
y = int(input()) # circulo
z = int(input()) # trapezio

triangulo = ((x * y) / 2)
circulo = (3.14159 * (z ** 2))
trapezio = (((x + y) * z) / 2)

print(f"{triangulo:.2f}")
print(f"{circulo:.2f}")
print(f"{trapezio:.2f}")