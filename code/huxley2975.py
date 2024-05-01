# Recebe o peso total da melancia
peso_total = int(input())

# Verifica se o peso total é par e se é possível encontrar duas fatias com pesos pares
if peso_total % 2 == 0 and peso_total > 2:
    print("YES")
else:
    print("NO")