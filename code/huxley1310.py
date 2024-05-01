votos_a = int(input())
votos_b = int(input())
votos_c = int(input())
nulos = int(input())

# soma = 100
# a = x

soma = (votos_a + votos_b + votos_c + nulos)
calculo1 = (votos_a * 100)
x_a = (calculo1 / soma)

calculo2 = (votos_b * 100)
x_b = (calculo2 / soma)

calculo3 = (votos_c * 100)
x_c = (calculo3 / soma)

calculo4 = (nulos * 100)
x_d = (calculo4 / soma)

print(f"Candidato A: {x_a:.0f}%")
print(f"Candidato B: {x_b:.0f}%")
print(f"Candidato C: {x_c:.0f}%")
print(f"Nulos: {x_d:.0f}%")