nota1 =float(input())
nota2 =float(input())
nota3 =float(input())

peso1a = 2
peso2a = 2
peso3a = 3

peso1b = 1
peso2b = 2
peso3b = 2


media = ((nota1 + nota2 + nota3) / 3)
print(f"{media:.2f}")

media_ponderada = (((nota1 * peso1a) + (nota2 * peso2a) + (nota3 * peso3a)) / (peso1a + peso2a + peso3a))
print(f"{media_ponderada:.2f}")

media_ponderada2 = (((nota1 * peso1b) + (nota2 * peso2b) + (nota3 * peso3b  )) / (peso1b + peso2b + peso3b))
print(f"{media_ponderada2:.2f}")