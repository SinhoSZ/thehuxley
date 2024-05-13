def vezes_subtrair(X, Y):
    # Verifica se X e Y são números naturais válidos
    if X < 1 or Y < 1:
        return
    
    # Inicializa um contador para contar quantas vezes Y pode ser subtraído de X
    contador = 0
    
    # Enquanto X for maior ou igual a Y, subtraia Y de X e incremente o contador
    while X >= Y:
        X -= Y
        contador += 1
    
    return contador # Retorna o valor do contador, que indica quantas vezes Y foi subtraído de X

# Programa principal
X = int(input())
Y = int(input())

# Chama a função vezes_subtrair e imprime o resultado
print(f"{vezes_subtrair(X, Y):.0f}")