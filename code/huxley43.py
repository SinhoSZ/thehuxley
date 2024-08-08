num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == num2 and num2 == num3:
    print("1") # 1 Se todos os números são iguais
elif num1 != num2 and num1 != num3 and num2 != num3:
    print("2") # 2 Se todos os números são diferentes
else:
    print("3") # 3 Se apenas dois números são iguais