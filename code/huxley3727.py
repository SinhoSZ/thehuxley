def media(nota1, nota2, nota3, nota4, nota5):
    soma = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
    return soma
    
faltas = int(input())
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
nota5 = float(input())

resultado = media(nota1, nota2, nota3, nota4, nota5)

if resultado >= 7 and faltas <= 5:
    print("APROVADO")
else:
    print("REPROVADO")