def divisao(a, b):
        calculo = a / b
        return calculo

def formatar_resultado(resultado):
    if isinstance(resultado, str):
        return resultado
    else:
        resultado_str = f"{resultado:.6f}"  # Formata com 6 casas decimais
        # Remove zeros à direita e o ponto decimal se for o caso
        resultado_str = resultado_str.rstrip('0').rstrip('.') if '.' in resultado_str else resultado_str
        return resultado_str

a = float(input())
b = float(input())

resultado = divisao(a, b)  # Chama a função

print(formatar_resultado(resultado))  # Exibe o resultado formatado