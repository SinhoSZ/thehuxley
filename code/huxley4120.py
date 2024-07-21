valor = int(input())

valor_desconto = valor * 0.10
desconto = (valor - valor_desconto)
parcela = valor / 3
comissao = 0.05 * desconto
comissao_parcela = 0.05 * valor

print(f"A vista com desconto de 10%: {desconto:.2f}")
print(f"Valor da parcela em 3x sem juros: {parcela:.2f}")
print(f"Comissao do vendedor a vista: {comissao:.2f}")
print(f"Comissao do vendedor a prazo: {comissao_parcela:.2f}")