def calcular_promocao_final_de_semana(apartamentos, diaria):
    # Calcula o valor promocional da diária (com 25% de desconto)
    valor_promocional = diaria * 0.75
    valor_promocional = round(valor_promocional, 2)
    return valor_promocional
    
def calcular_arrecadacao_100(apartamentos, diaria):
    # Calcula o valor total a ser arrecadado com 100% de ocupação (para dois dias)
    total_100_ocupacao = resultado * apartamentos * 2
    total_100_ocupacao = round(total_100_ocupacao, 2)
    return total_100_ocupacao
    
def calcular_arrecadacao_70(apartamentos, diaria):
    # Calcula o valor total a ser arrecadado com 70% de ocupação (para dois dias)
    total_70_ocupacao = resultado * (apartamentos * 0.70) * 2
    total_70_ocupacao = round(total_70_ocupacao, 2)
    return total_70_ocupacao
    
def calcular_perca_100(apartamentos, diaria):
    # Calcula o valor que o hotel deixará de arrecadar devido à promoção (para dois dias)
    valor_deixado_de_arrecadar = (diaria * apartamentos * 2) - resultado1
    valor_deixado_de_arrecadar = round(valor_deixado_de_arrecadar, 2)
    return valor_deixado_de_arrecadar
    
# Exemplo de uso da função
apartamentos = int(input())
diaria = float(input())

resultado = calcular_promocao_final_de_semana(apartamentos, diaria)
resultado1 = calcular_arrecadacao_100(apartamentos, diaria)
resultado2 = calcular_arrecadacao_70(apartamentos, diaria)
resultado3 = calcular_perca_100(apartamentos, diaria)

print(f"{resultado}")
print(f"{resultado1}")
print(f"{resultado2}")
print(f"{resultado3}")