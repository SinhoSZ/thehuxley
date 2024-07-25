# Entrada de segundos
Segundos = int(input())

# Cálculo de horas, minutos e segundos
horas = Segundos // 3600
restante = Segundos % 3600
minutos = restante // 60
segundos = restante % 60

# Saída formatada
print(f"{horas}:{minutos}:{segundos}")
