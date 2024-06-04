salario = float(input())

if salario <= 280:
   calculo = salario * 0.20
   soma = salario + calculo
   print(soma)
elif salario <= 700:
   calculo = salario * 0.15
   soma = salario + calculo
   print(soma)
elif salario <= 1500:
   calculo = salario * 0.10
   soma = salario + calculo
   print(soma)
elif salario > 1500:
   calculo = salario * 0.05
   soma = salario + calculo
   print(soma)
 