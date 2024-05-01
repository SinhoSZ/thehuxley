while True: #Isso cria um loop infinito. Enquanto a condição True for verdadeira (o que é sempre), o código dentro do loop será executado repetidamente.
    codigo = int(input())

    if codigo == 0:
        print("Informe o codigo do aluno: (0 para encerrar o programa)")
        break   # break: Esta instrução é usada para sair do loop while quando uma nota válida é inserida.
    else:
        nota1 = float(input())
        nota2 = float(input())
        nota3 = float(input())
        media = ((nota1 + nota2 + nota3) / 3)
        print("Informe o codigo do aluno: (0 para encerrar o programa)")
        print("Informe a primeira nota do aluno:")
        print("Informe a segunda nota do aluno:")
        print("Informe a terceira nota do aluno:")
        print(f"Media do aluno: {media:.1f}" if media.is_integer() else f"Media do aluno: {media:.2f}")