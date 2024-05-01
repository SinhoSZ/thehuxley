# Recebendo as entradas do usuário
diaria = int(input())
km_diario = int(input())

# Definindo os valores das taxas e da cota de quilometragem
valor_diaria = 90 # R$
taxa_extra_km = 12 # KM
cota_km = 100 # km por dia

# Calculando o valor total das diárias
valor_total_diaria = (diaria * valor_diaria)

# Calculando a quantidade de quilômetros extras
km_extra = max(km_diario -(diaria * cota_km),0)

# Calculando o valor total dos quilômetros extras
valor_km_extra = (km_extra * taxa_extra_km)

# Calculando o valor total a ser pago
valor_total = (valor_total_diaria + valor_km_extra)

# # Exibindo o valor total a ser pago
print(f"{valor_total:.2f}")