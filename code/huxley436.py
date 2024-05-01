mulheres = int(input())
homens = int(input())

vinho = 10 # para mulher
panetone = 8.50 # para homem

custo_m = (mulheres * vinho)
custo_h = (homens * panetone)

total = (custo_m + custo_h)
media = ((total) / (mulheres + homens))

print(f"{total:.2f}")
print(f"{media:.2f}")