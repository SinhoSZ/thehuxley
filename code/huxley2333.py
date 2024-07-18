num1 = float(input())
num2 = float(input())
nome = input()

if nome == "soma":
    soma = num1 + num2
    print(f"resultado = {soma:.2f}")
elif nome == "subtracao":
    subtracao = num1 - num2
    print(f"resultado = {subtracao:.2f}")
elif nome == "divisao":
    divisao = num1 / num2
    print(f"resultado = {divisao:.2f}")
elif nome == "multiplicacao":
    multiplicacao = num1 * num2
    print(f"resultado = {multiplicacao:.2f}")