Alice = int(input())
Beto = int(input())
Clara = int(input())

if Alice == Beto and Clara != Alice:
    print("C")
elif Alice == Clara and Beto != Alice:
    print("B")
elif Beto == Clara and Clara != Alice:
    print("A")
elif Alice == Beto == Clara:
    print("*")
