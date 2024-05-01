broas = int(input())
paes = int(input())

broa = 1.50
pao = 0.20

pao_v_dia = (pao * paes)
broa_v_dia = (broa * broas)
venda_diaria = (pao_v_dia + broa_v_dia)
poupança = (venda_diaria * 0.10)
print(f"O valor a ser guardado na poupança será R$ {poupança:.2f}")