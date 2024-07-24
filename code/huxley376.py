livros = int(input())
alunos = int(input())
soma = alunos / livros

if soma > 0 and soma <=8:
    print("A")
elif soma >= 9 and soma <= 12:
    print("B")
elif soma >= 13 and soma <= 18:
    print("C")
else:
    print("D")