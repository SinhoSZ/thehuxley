def verifica_par(numero):
    if numero % 2 == 0:
        return 1
    else:
        return 0

def main():
    numero = int(input())
    
    # Chama a função verifica_par para verificar se o número é par
    resultado = verifica_par(numero)
    
    # Exibe a mensagem conforme o resultado
    if resultado == 1:
        print("par")
    else:
        print("nao par")

# Executa o programa principal
if __name__ == "__main__":
    main()