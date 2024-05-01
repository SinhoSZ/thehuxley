dinheiro = float(input())

primeiro = dinheiro * 0.6
premiacao1 = primeiro

segundo = dinheiro * 0.3
premiacao2 = segundo

terceiro = dinheiro * 0.1
premiacao3 = terceiro

print("Digite o valor total do premio em dinheiro:")
print(f"Premio para o 1 lugar: R$ {premiacao1:.0f}" if premiacao1.is_integer() else f"Premio para o 1 lugar: R$ {premiacao1:.1f}")
print(f"Premio para o 2 lugar: R$ {premiacao2:.0f}" if premiacao2.is_integer() else f"Premio para o 2 lugar: R$ {premiacao2:.1f}")
print(f"Premio para o 3 lugar: R$ {premiacao3:.0f}" if premiacao3.is_integer() else f"Premio para o 3 lugar: R$ {premiacao3:.1f}")

# OBSERVAÇÃO NO PRINT