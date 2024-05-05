nota1 = float(input()) # novela
nota2 = float(input()) # filme
nota3 = float(input()) # futebol
nota4 = float(input()) # novela
nota5 = float(input()) # filme

media = ((nota1 + nota2 + nota3 + nota4 + nota5) / 5)

segunda_quinta = nota1 + nota4
quarta = nota3
terça_sexta = nota2 + nota5

if nota1 > nota2 and nota1 > nota3 and nota1 > nota4 and nota1 > nota5:
    print(f"{media:.2f}")
    print("NOVELA")
elif nota2 > nota1 and nota2 > nota3 and nota2 > nota4 and nota2 > nota5:
    print(f"{media:.2f}")
    print("FILME")
elif nota3 > nota2 and nota3 > nota1 and nota3 > nota4 and nota3 > nota5:
    print(f"{media:.2f}")
    print("FUTEBOL")
elif nota4 > nota2 and nota4 > nota3 and nota4 > nota1 and nota4 > nota5:
    print(f"{media:.2f}")
    print("NOVELA")
elif nota5 > nota2 and nota5 > nota3 and nota5 > nota4 and nota5 > nota1:
    print(f"{media:.2f}")
    print("FILME")