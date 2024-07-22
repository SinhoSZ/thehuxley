vagas = int(input())
vagas_totais = 42
preco_unitario = 1.75
pode_ganhar = ((vagas_totais * preco_unitario) - (vagas * preco_unitario))
print(f"{pode_ganhar:.2f}")