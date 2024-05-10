def encontrar_posicao(caractere, string):
    # Verifica se o caractere está presente na string
    if caractere in string:
        # Encontra e retorna o índice da primeira ocorrência do caractere na string
        return string.find(caractere)
    else:
        return -1   # Se o caractere não estiver presente na string, retorna -1

# Recebe os dados do usuário
string = input()
caractere = input()

posicao = encontrar_posicao(caractere, string) # Chama a função para encontrar a posição do caractere na string

print(posicao) # Exibe o resultado