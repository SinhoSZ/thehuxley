# Entrada de três números inteiros
a = int(input())
b = int(input())
c = int(input())

# Ordena os números em ordem decrescente
if a >= b and b >= c:
    print(f"{a}")
    print(f"{b}")
    print(f"{c}")
elif a >= c and c >= b:
    print(f"{a}")
    print(f"{c}")
    print(f"{b}")
elif b >= a and a >= c:
    print(f"{b}")
    print(f"{a}")
    print(f"{c}")
elif b >= c and c >= a:
    print(f"{b}")
    print(f"{c}")
    print(f"{a}")
elif c >= a and a >= b:
    print(f"{c}")
    print(f"{a}")
    print(f"{b}")
else: # c >= b and b >= a
    print(f"{c}")
    print(f"{b}")
    print(f"{a}")
