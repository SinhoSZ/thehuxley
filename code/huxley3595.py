numero = input()  # Recebe o número como uma string

# Verifica se o número tem quatro dígitos e se todos são diferentes de zero
if len(numero) == 4 and "0" not in numero:
# Verifica se o comprimento da string numero é igual a 4, ou seja, se o número tem quatro dígitos.
    print("Pode")
else:
    print("Nao pode")