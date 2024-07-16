#Obs
import math

num = float(input())

piso = math.floor(num)
teto = math.ceil(num)
raiz = math.sqrt(num)
seno = math.sin(num)
cosseno = math.cos(num)
pot3 = (num ** 3)


print(f"numero={num:.6f}")
print(f"piso={piso:.6f}")
print(f"teto={teto:.6f}")
print(f"raiz={raiz:.6f}")
print(f"seno={seno:.6f}")
print(f"cosseno={cosseno:.6f}")
print(f"pot3={pot3:.6f}")