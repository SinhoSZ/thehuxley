# Recebe a lista de inteiros do usuário no formato [1, 4, -9, 0, 6]
entrada = input()

# Remove os colchetes da entrada e converte os elementos separados por vírgula em uma lista de strings
elementos = entrada[1:-1].split(',')

# Converte os elementos da lista de strings para inteiros
lista = [int(elemento) for elemento in elementos]

# Inicializa o maior elemento como o primeiro elemento da lista
maior = lista[0]

# Verifica cada elemento da lista
for elemento in lista:
    if elemento > maior:
        maior = elemento

# Imprime o maior elemento encontrado
print(maior)