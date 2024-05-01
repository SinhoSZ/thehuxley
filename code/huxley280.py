nome = input()
salario_fixo = float(input())
total_vendas = float(input())

comissao = 0.15 # 15%

calculo_comisao1 = (total_vendas * comissao)
calculo_comisao2 = (salario_fixo + calculo_comisao1)

print(f"TOTAL = R$ {calculo_comisao2:.2f}")
