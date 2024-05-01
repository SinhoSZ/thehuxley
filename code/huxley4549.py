linha = input() # Exemplo de entrada: "2"
lista = linha.split() # ["2"]
fatura = float(lista[0])

marco = float(fatura / 2)
juros = 6.5 # 6.5%
juro_proximo_mes = ((marco / 100) * juros)
abril = float(marco + juro_proximo_mes )

print(f"Valor total da fatura: R$ {fatura:.2f}")
print(f"Valor a pagar em Marco: R$ {marco:.2f}")
print(f"Valor a pagar em Abril: R$ {abril:.2f}")
