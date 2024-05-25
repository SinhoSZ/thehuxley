ph = int(input())

if ph == 7:
    print("Digite o pH da solucao:")
    print("Essa solucao e neutra.")
elif ph > 7 and ph <= 14:
    print("Digite o pH da solucao:")
    print("Essa solucao e basica.")
elif ph < 7 and ph >= 0:
    print("Digite o pH da solucao:")
    print("Essa solucao e acida.")
else:
    print("Digite o pH da solucao:")
    print("Valor deve estar entre 0 e 14.")