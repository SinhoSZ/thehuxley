# Recebendo as escolhas do cliente em letras minúsculas
comida = input().lower()
bebida = input().lower()

# Verificando as escolhas e atribuindo os valores correspondentes
if comida == 'lasanha':
    valor_comida = 8.00
elif comida == 'Lasanha':
     valor_comida = 8.00
elif comida == 'estrogonofe':
    valor_comida = 11.00
elif comida == 'Estrogonofe':
    valor_comida = 11.00
else:
    print("Opção de comida inválida!")

if bebida == 'refrigerante':
    valor_bebida = 3.00
elif bebida == 'refrigerante':
    valor_bebida = 3.00
elif bebida == 'suco':
    valor_bebida = 2.50
elif bebida == 'Suco':
    valor_bebida = 2.50
else:
    print("Opção de bebida inválida!")

# Calculando o valor total a ser pago
valor_total = valor_comida + valor_bebida

# Exibindo o valor total
print(f"{valor_total:.2f}")