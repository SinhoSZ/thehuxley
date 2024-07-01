num = int(input())

anos = num // 365
resto = num % 365
semanas = resto // 7
dias = resto % 7

print(f"{anos} ano(s), {semanas} semana(s) e {dias} dia(s)")