altura = float(input())
idade = int(input())

brinquedos_disponiveis = []

if altura >= 1.50 and idade >= 12:
    brinquedos_disponiveis.append("Barca Viking")
if altura >= 1.40 and idade >= 14:
    brinquedos_disponiveis.append("Elevator of Death")
if altura >= 1.70 or idade >= 16:
    brinquedos_disponiveis.append("Final Killer")

num_brinquedos = len(brinquedos_disponiveis)

print("Digite a altura em m:")
print("Digite a idade:")
print(f"Voce pode andar em {num_brinquedos} brinquedos, sendo eles:")
for brinquedo in brinquedos_disponiveis:
    print(brinquedo)