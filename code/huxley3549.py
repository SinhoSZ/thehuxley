zilde = int(input()) # quanto Zilde pode gastar.
led = int(input())   # quanto Led pode gastar.
forma, quantidade = map(int, input().split())   # C = forma de pagamento (0-> cartão de crédito e 1-> dinheiro ou débito)
preco_esfiha = int(input()) # o preço da esfiha.                   

desc1 = 0.05 # credito
desc2 = 0.15 # dinheiro ou debito

soma_zilde_led = (zilde + led) # tal do dinheiro
preco_total = preco_esfiha * quantidade

if soma_zilde_led >= preco_total:
    if forma == 0:
        desconto = preco_total * desc1
    elif forma == 1:
        desconto = preco_total * desc2

    preco_com_desconto = preco_total - desconto

    if soma_zilde_led >= preco_com_desconto:
        print("faz um ifood!")
    else:
        print("pede menos que as esfihas nao vao acabar hoje!")
else:
    print("pede menos que as esfihas nao vao acabar hoje!")