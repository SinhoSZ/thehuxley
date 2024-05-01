reais = float(input())

dolar = 3.87
euro = 4.35

reais_dolar = (reais / dolar)
resultado_dolar = reais_dolar
reais_euro = (reais / euro)
resultado_euro = reais_euro

print("Digite o valor em reais:")
print(f"Valor convertido em dolar: {resultado_dolar:.2f}")
print(f"Valor convertido em euro: {resultado_euro:.2f}")