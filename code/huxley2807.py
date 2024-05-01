dias = input() # "2 3"
lista = dias.split() # ["2","3"]
a = int(lista[0]) # 2

km = input() # "2 3"
lista = km.split() # ["2","3"]
b = int(lista[0]) # 2

km_rodados = 0.01
dias_rodados = 30

percentual = 10 # 10%

valor_a_ser_pago = ((a * dias_rodados) + (b * km_rodados))
porcentagem = ((valor_a_ser_pago / 100) * percentual)

total = (valor_a_ser_pago - porcentagem)
print("Digite a quantidade de dias de locacao:")
print("Digite a quantidade de km rodados:")
print(f"Valor a pagar pelo aluguel: R$ {total:.6f}") 
    