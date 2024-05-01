 # Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True: #Isso cria um loop infinito. Enquanto a condição True for verdadeira (o que é sempre), o código dentro do loop será executado repetidamente.
    nota = float(input())
    if 0 <= nota <= 10:
        print("Informe uma nota entre 0 e 10:")
        break   # break: Esta instrução é usada para sair do loop while quando uma nota válida é inserida.
    else:
        print("Informe uma nota entre 0 e 10:")
        print("Valor invalido")