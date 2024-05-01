nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

peso_1 = 2
peso_2 = 2
peso_3 = 3
peso_4 = 3

media_ponderada = (((nota1 * peso_1) +(nota2 * peso_2) + (nota3 * peso_3) + (nota4 * peso_4))/(peso_1 + peso_2 + peso_3 + peso_4))
numero_formatado = f"{media_ponderada:.2f}"
print(f"A média ponderada será: {numero_formatado}")  # Saída: 5.86