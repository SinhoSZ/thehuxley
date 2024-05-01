num = int(input())

divisao = ((num + 1) / 2)

if num >= 1:
    print("Digite um numero positivo:")
    print(f"Media de 1 ate {num}: {divisao:.0f}" if divisao.is_integer() else f"Media de 1 ate {num}: {divisao:.1f}")
else:
    print("Digite um numero positivo:")
    print("Apenas valores positivos")