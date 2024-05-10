def remover_prefixo_des(palavra):
    if palavra.startswith("des"):
        return palavra.replace("des", "", 1)
    else:
        return palavra

# Lê a palavra do usuário
palavra = input()

# Corrige a palavra e exibe o resultado
print(remover_prefixo_des(palavra))