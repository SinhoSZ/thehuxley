a = float(input())
b = float(input())

if a > b:
    dobro = a * 2
    print(f"{dobro:.2f}")
elif b > a:
    dobro = b * 2
    print(f"{dobro:.2f}")
else:
    dobro = b * 2
    print(f"{dobro:.2f}")