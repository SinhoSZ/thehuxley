def convert_seconds():
    total_seconds = int(input())

    hours = total_seconds // 3600 # Calcula o número de horas

    minutes = (total_seconds % 3600) // 60 # Calcula o número de minutos restantes

    seconds = total_seconds % 60 # Calcula o número de segundos restantes

    # Exibe o resultado na forma esperada
    print(f"{hours} h {minutes} m {seconds} s")

# Executa a função de conversão
convert_seconds()
