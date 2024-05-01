nota1 = float(input())  # Lê o primeiro número
nota2 = float(input())  # Lê o segundo número
nota3 = float(input())  # Lê o terceiro número

media = ((nota1 + nota2 + nota3) / 3)

if media >= 7:
    print("aprovado")
elif media >= 3.0 and media < 7.0:
    print("prova final")
elif media < 3.0:
    print("reprovado")

