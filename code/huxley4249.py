conta_energia = float(input())
custo = 1.50

valor_da_conta = conta_energia * custo
valor_com_desconto = (valor_da_conta - (valor_da_conta * 0.15))

print(f"Digite o valor real em KWh consumido:")
print(f"Valor a ser pago: R$ {valor_da_conta:.2f} reais")
print(f"Valor a ser pago com desconto: R$ {valor_com_desconto:.2f} reais")