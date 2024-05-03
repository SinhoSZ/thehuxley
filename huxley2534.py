valor = int(input())

if valor <= 19:
    porcentagem = valor * 0.45
    total = porcentagem + valor
    print("Digite o valor de compra do produto:")
    print(f"O produto deve ser vendido a R$ {total:.0f}" if total.is_integer() else f"O produto deve ser vendido a R$ {total:.1f}")
else:
    porcentagem = valor * 0.30
    total = porcentagem + valor
    print("Digite o valor de compra do produto:")
    print(f"O produto deve ser vendido a R$ {total:.0f}" if total.is_integer() else f"O produto deve ser vendido a R$ {total:.1f}")
          
   