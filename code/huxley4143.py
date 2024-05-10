num1 = int(input())
num2 = int(input())
simbolo = input()

if simbolo == "/":
    calculo = (num1 / num2)
    print(f"{num1:.2f} / {num2:.2f} = {calculo:.2f}")
elif simbolo == "*":
    calculo = (num1 * num2)
    print(f"{num1:.2f} * {num2:.2f} = {calculo:.2f}")
elif simbolo == "-":
    calculo = (num1 - num2)
    print(f"{num1:.2f} - {num2:.2f} = {calculo:.2f}")
elif simbolo == "+":
    calculo = (num1 + num2)
    print(f"{num1:.2f} + {num2:.2f} = {calculo:.2f}")
else:
    print(f"A operacao {simbolo} eh invalida!")