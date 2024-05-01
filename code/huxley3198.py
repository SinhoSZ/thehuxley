num1 = int(input())
num2 = int(input())

divisao = num1 / num2

print(f"{divisao:.1f}" if divisao.is_integer() else f"{divisao:.2f}")