def MDC(a, b):
    while b:
        a, b = b, a % b
    return a

# EXEMPLO DE USO
num1 = int(input())
num2 = int(input())

resultado = MDC(num1, num2)
print(f"MDC={resultado}")