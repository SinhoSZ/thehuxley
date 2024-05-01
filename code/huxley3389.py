preco = int(input())
b = input().lower() # Converte para minúsculas

if b in ("e", "a", "n"):  # Verifica se a entrada está correta
    if b == "e" :  # Se o cliente é estudante
        calculo_desconto1 = (preco * 0.50)
        desconto1 = preco - calculo_desconto1
        print(f"Preco com desconto: R${desconto1:.2f}")
        print("Categoria: Estudante")
    elif b == "a" :  # Se o cliente é aposentado
        calculo_desconto2 = (preco * 0.30)
        desconto2 = preco - calculo_desconto2
        print(f"Preco com desconto: R${desconto2:.2f}")
        print("Categoria: Aposentado")
    elif b == "n" :  # Se o cliente não é estudante nem aposentado
        print(f"Preco sem desconto: R${preco:.2f}")
else:
    print("Categoria invalida!")
