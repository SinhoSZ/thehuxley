nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = ((nota1 + nota2 + nota3)/3)
numero_formatado = f"{media:.2f}"
print(numero_formatado)  # Saída: 6.33

peso_1a = 2
peso_1b = 2
peso_1c = 3

media_ponderada = (((nota1 * peso_1a) +(nota2 * peso_1b) + (nota3 * peso_1c))/(peso_1a + peso_1b + peso_1c))
numero_formatado = f"{media_ponderada:.2f}"
print(numero_formatado)  # Saída: 5.86

peso_2a = 1
peso_2b = 2
peso_2c = 2

media_ponderada2 = (((nota1 * peso_2a) +(nota2 * peso_2b) + (nota3 * peso_2c))/(peso_2a + peso_2b + peso_2c))
numero_formatado = f"{media_ponderada2:.2f}"
print(numero_formatado)  # Saída: 5.60
