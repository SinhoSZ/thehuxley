peso_do_prato = input()
lista = peso_do_prato.split() # ["2","3"]
peso = float(lista[0]) # 2

kilos = 20

total = (20 * peso)
total_a_pagar = (f"{total:.2f}")
print(f"O valor do prato será: R$ {total_a_pagar}")