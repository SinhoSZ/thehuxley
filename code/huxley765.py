valores = input().split() # Recebe a lista de valores inteiros
valores = [int(x) for x in valores] # Converte os valores para inteiros

media = sum(valores) / len(valores) # Calcula a m�dia dos valores
print(f"Media = {media:.1f}")