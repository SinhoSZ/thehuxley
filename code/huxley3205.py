conta = float(input())
divisao = int(conta // 3)
calculando = conta - (divisao * 2)

# Verifica se o valor restante tem apenas uma casa decimal
if calculando * 10 % 1 == 0:
    restante_formatado = f"{calculando:.1f}"
else:
    restante_formatado = f"{calculando:.2f}"

print(f"{divisao:.1f}")
print(f"{divisao:.1f}")
print(f"{restante_formatado}")