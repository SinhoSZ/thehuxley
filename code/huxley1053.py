altura = float(input())
raio = float(input())

pi = 3.14

# O volume de um cilindro é π r² h, e sua área de superfície é 2π r h + 2π r².

volume = (pi * (raio**2) * altura)
area = (((2 * pi) * raio) * altura) + ((2 * pi) * raio ** 2)

print(f'{volume:.2f}')
print(f'{area:.2f}')

# 6.11    # 3217.44
# 12.95   # 1550.07