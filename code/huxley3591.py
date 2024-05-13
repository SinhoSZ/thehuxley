letra = input()

if letra.lower() in ['a','e', 'i', 'o', 'u']:
    print(f"A letra {letra} eh uma vogal")
elif letra.isalpha(): # verifica se a letra é um caractere alfabético.
    print(f"A letra {letra} eh uma consoante")
else:
    print(f"O caractere {letra} nao eh nem consoante nem vogal")
