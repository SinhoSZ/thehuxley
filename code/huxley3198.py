def divisao(num1, num2):
        calculo = num1 / num2
        return calculo

def formatar_resultado(resultado):
    if resultado.is_integer():
        return f"{resultado:.1f}"
    else:
        resultado_str = f"{resultado:.10f}".rstrip('0')
        parte_decimal = resultado_str.split('.')[1]
        if len(parte_decimal) == 1:
            return f"{resultado:.1f}" # Se a parte decimal tiver apenas um dígito, formata com uma casa decimal 
        elif len(parte_decimal) == 2:
            return f"{resultado:.2f}" # Se a parte decimal tiver dois dígitos, formata com duas casas decimais
        else:
            return f"{resultado:.2f}" # Se a parte decimal tiver mais de dois dígitos, formata com duas casas decimais

num1 = int(input())
num2 = int(input())

resultado = divisao(num1, num2)

if resultado is not None:
    print(formatar_resultado(resultado))