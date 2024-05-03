def encontrar_maior(V, W, X, Y, Z):
    # Encontra o maior valor entre os cinco números
    maior = max(V, W, X, Y, Z)
    return maior

# Programa principal
def main():
    # Solicita ao usuário que insira cinco números reais distintos
    V = float(input())
    W = float(input())
    X = float(input())
    Y = float(input())
    Z = float(input())

    maior_numero = encontrar_maior(V, W, X, Y, Z) # Chama a função para encontrar o maior número

    # Exibe o resultado
    print(f"{maior_numero:.2f}")

if __name__ == "__main__":
    main()