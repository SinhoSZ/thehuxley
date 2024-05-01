#ERROR

num1 = int(input())
num2 = int(input())

divisão = (num1 / num2)
resultado = divisão

print(f"{resultado:.0f}" if resultado.is_integer() else f"{resultado:.2f}")