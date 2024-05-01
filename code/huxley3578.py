def adicao(x, y):   # Função para adição
    return x + y

def subtracao(x, y): # Função para subtração
    return x - y

def multiplicacao(x, y): # Função para multiplicação
    return x * y

def divisao(x, y): # Função para divisão
    if y == 0:
        return "Erro! Divisão por zero não é permitida."
    else:
        return x / y

# Função principal
def main():
    # Solicitar entrada do usuário
    num1 = float(input(""))
    num2 = float(input(""))

    # Calcular e imprimir resultados
    print(f"{adicao(num1, num2):.2f}")
    print(f"{subtracao(num1, num2):.2f}")
    print(f"{multiplicacao(num1, num2):.2f}")
    print(f"{divisao(num1, num2):.2f}")

# Chamar a função principal
if __name__ == "__main__":
    main()