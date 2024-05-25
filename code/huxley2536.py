salario = float(input())
emprestimo = float(input())
prestacoes = int(input())

calculo = salario * 0.30
calculo1 = emprestimo / prestacoes

if calculo1 > calculo:
    print("Digite o salario:")
    print("Digite o valor do emprestimo:")
    print("Digite o numero de prestacoes:")
    print("O emprestimo nao pode ser concedido")
else:
    print("Digite o salario:")
    print("Digite o valor do emprestimo:")
    print("Digite o numero de prestacoes:")
    print("O emprestimo pode ser concedido")