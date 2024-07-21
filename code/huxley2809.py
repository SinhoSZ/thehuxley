num = int(input())

if num < 0: # Verifica se o número é negativo
    numero_revertido_str = str(num)[1:][::-1] # Reverte a parte numérica, sem o sinal negativo
    # Obter o primeiro dígito e adicionar o sinal negativo
    primeiro_digito = '-' + numero_revertido_str[0]
else:
    # Reverte o número normalmente
    numero_revertido_str = str(num)[::-1]
    # Obter o primeiro dígito
    primeiro_digito = numero_revertido_str[0]

print("Digite um numero:")
print(f"Algarismo das unidades: {primeiro_digito}")