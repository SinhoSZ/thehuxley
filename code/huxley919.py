
#ERROR

Saldo_inicial = float(input())
Total_de_débitos = float(input())
Total_de_créditos = float(input())


conta = ((Saldo_inicial - Total_de_débitos) + Total_de_créditos)
resultado = conta

print("Informe o saldo inicial do cliente:")
print("Informe o total de debitos adquiridos pelo cliente:")
print("Informe o total de creditos adquiridos pelo cliente:")

if resultado > 0:
    print(f"Saldo positivo em R$ {resultado}")
elif resultado == 0:
    print("Saldo Zero")
elif resultado < 0:
    print(f"Saldo negativo em R$ {resultado}")