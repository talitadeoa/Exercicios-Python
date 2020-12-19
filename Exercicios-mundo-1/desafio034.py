#Um programa que calcula o aumento do salário

salario = float(input('Digite o valor do seu salário atual... '))

if salario <= 1250:
    salario = salario + (salario*15/100)
else:
    salario = salario + (salario*10/100)

print('Seu novo salário será {}'. format(salario))