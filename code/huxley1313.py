num1 = float(input())
num2 = float(input())
num3 = float(input())

if num1 < num2 and num1 < num3:
    print("Primeiro produto")
elif num2 < num1 and num2 < num3:
    print("Segundo produto")
elif num3 < num1 and num3 < num2:
    print("Terceiro produto")