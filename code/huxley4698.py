def somar(a, b):
    resultado = a + b
    if resultado.is_integer():
        print(f"O resultado de {a:.1f} + {b:.1f} eh {int(resultado)}")
    else:
        print(f"O resultado de {a:.1f} + {b:.1f} eh {resultado:.1f}")

a = float(input())
b = float(input())

somar(a, b)