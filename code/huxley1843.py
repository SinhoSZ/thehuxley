entrada = input()  # Recebe a entrada como uma string
entrada = entrada.strip("[]")  # Remove os colchetes
numeros = entrada.split(",")  # Divide a string nos espaços e converte em uma lista de substrings

valores = list(map(int, numeros))  # Converte as substrings em números inteiros e coloca-os em uma lista

media = sum(valores) / len(valores)  # Calcula a média dos valores
maior = max(valores)  # Encontra o valor máximo
menor = min(valores)  # Encontra o valor mínimo

print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Media: {media:.2f}")