diaria = int(input())    # Recebendo as entradas do usuário
km_diario = int(input())

# Verifica se os valores são negativos
if diaria < 0 or km_diario < 0:
    print("Digite a quantidade de dias de locacao:")
    print("Digite a quantidade de km rodados:")
    print("Valor invalido")
else:
    # Se os valores forem válidos, continue com o cálculo
    valor_diaria = 90
    taxa_extra_km = 12        # Definindo os valores das taxas e da cota de quilometragem
    cota_km = 100

    valor_total_diaria = diaria * valor_diaria         # Calculando o valor total das diárias
    km_extra = max(km_diario - (diaria * cota_km), 0)  # Calculando a quantidade de quilômetros extras
    valor_km_extra = km_extra * taxa_extra_km          # Calculando o valor total dos quilômetros extras
    valor_total = valor_total_diaria + valor_km_extra  # Calculando o valor total a ser pago

    print("Digite a quantidade de dias de locacao:")
    print("Digite a quantidade de km rodados:")
    print(f"Valor total a ser pago em reais: {valor_total:.0f}")