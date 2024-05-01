h = input() # "2 3"
lista = h.split() # ["2","3"]
horas = int(lista[0]) # 2

m = input() # "2 3"
lista = m.split() # ["2","3"]
minutos = int(lista[0]) # 2

s = input() # "2 3"
lista = s.split() # ["2","3"]
segundos = int(lista[0]) # 2

horas_em_segundos = ((horas * 60) * 60)
    #print(horas_em_segundos)
minutos_em_segundos = (minutos * 60)


total_de_segundos = (horas_em_segundos + minutos_em_segundos + segundos)
print(total_de_segundos)