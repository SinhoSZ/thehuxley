salario = int(input())
aumento1 = 0.10
aumento2 = 0.07
aumento3 = 0.05

if salario > 500:
    salario_com_aumento1 = salario * aumento1
    atualização1 = salario_com_aumento1 + salario
    print(f"{atualização1:.2f}")
elif salario > 300:
    salario_com_aumento2 = salario * aumento2
    atualização2 = salario_com_aumento2 + salario
    print(f"{atualização2:.2f}")
elif salario <= 300:
    salario_com_aumento3 = salario * aumento3
    atualização3 = salario_com_aumento3 + salario
    print(f"{atualização3:.2f}")
