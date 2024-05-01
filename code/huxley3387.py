habilitaçao = int(input())

falta = (18 - habilitaçao)
tem = (habilitaçao - 18)


if habilitaçao >= 18:
    print("Voce ja pode tirar habilitacao!")
    print(f"Voce tem direito a habilitacao ha {tem} ano(s)")
else:
    print(f"Voce precisa esperar mais {falta} ano(s)!")
