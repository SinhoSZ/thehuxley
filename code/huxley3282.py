salario = float(input())
percentual = float(input())

percentual_aumento = ((salario / 100) * percentual)
total = (percentual_aumento + salario)

print(f"{percentual_aumento:.2f}")
print(f"{total:.2f}")
