cedula = int(input())

cem = cedula // 100
restante = cedula % 100
cinquenta = restante // 50
restante = restante % 50
vinte = restante // 20
restante = restante % 20
dez = restante // 10
restante = restante % 10
cinco = restante // 5
restante = restante % 5
dois = restante // 2
restante = restante % 2
um = restante // 1

print("Digite o valor inteiro:")
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} moeda(s) de R$ 1,00")
