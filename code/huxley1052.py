def calcular_diagonais(lados):
    if lados < 3:
        return 0  # Um polígono deve ter pelo menos 3 lados
    diagonais = (lados * (lados - 3)) // 2
    return diagonais

lados = int(input())
diagonais = calcular_diagonais(lados)
print(f"{diagonais}")
