ph = float(input())

if ph == 7:
    print("Digite o pH da solucao:")
    print("Solucao neutra")
elif ph > 7 and ph <= 14:
    print("Digite o pH da solucao:")
    print("Solucao basica")
elif ph < 7 and ph >= 0:
    print("Digite o pH da solucao:")
    print("Solucao acida")
else:
    print("Digite o pH da solucao:")
    print("Valor do pH deve estar entre 0 e 14")