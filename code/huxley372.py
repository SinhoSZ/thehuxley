salario = float(input())
horas_extra = int(input())

calculo_hora_extra1 = (salario * 0.05)
calculo_hora_extra2 = (horas_extra * calculo_hora_extra1)
salario_final = (calculo_hora_extra2 + salario)

print(f"{salario_final:.2f}")