import math

largura = float(input())
altura = float(input())

diagonal = math.sqrt(largura**2 + altura**2)
print(f"{diagonal:.1f}")