salario = float(input())
bonus = salario * 0.75


if bonus <= 2000:
    print("ARGENTINA")
elif bonus <= 3000:
    print("ESPANHA")
elif bonus >= 3001:
    print("ALEMANHA")
