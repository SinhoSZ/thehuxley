numero = int(input())  # Valor fixo para R$ 78

RS_100 = numero // 100
numero %= 100  # Atualiza o valor de numero para o resto após divisão por 100

RS_50 = numero // 50
numero %= 50  # Atualiza o valor de numero para o resto após divisão por 50

RS_20 = numero // 20
numero %= 20  # Atualiza o valor de numero para o resto após divisão por 20

RS_10 = numero // 10
numero %= 10  # Atualiza o valor de numero para o resto após divisão por 10

RS_5 = numero // 5
numero %= 5  # Atualiza o valor de numero para o resto após divisão por 5

RS_2 = numero // 2
numero %= 2  # Atualiza o valor de numero para o resto após divisão por 2

RS_1 = numero  # O resto após divisão por 1 é o próprio numero

# Mostra os resultados
print(f"{RS_100}")
print(f"{RS_50}")
print(f"{RS_20}")
print(f"{RS_10}")
print(f"{RS_5}")
print(f"{RS_2}")
print(f"{RS_1}")