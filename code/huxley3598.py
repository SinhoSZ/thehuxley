mae = int(input())
filho1 = int(input())
filho2 = int(input())

a = filho1
b = filho2
c = mae - (a + b)

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)