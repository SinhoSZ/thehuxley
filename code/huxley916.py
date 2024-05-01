
while True: #Isso cria um loop infinito. Enquanto a condição True for verdadeira (o que é sempre), o código dentro do loop será executado repetidamente.
    quantidade = int(input())
    if quantidade < 0:
        print("Digite um numero (negativo para parar o programa):")
        break   # break: Esta instrução é usada para sair do loop while quando uma nota válida é inserida.
    else:
        print("Digite um numero (negativo para parar o programa):")
        print(f"Numero: {quantidade}")

