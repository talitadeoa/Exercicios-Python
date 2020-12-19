#Um algoritimo que calcula o salario de um funciomário mais 15%

salario = float(input('Qual é o salário atual? '))

novo_salario = salario + (salario*15/100)

#p = salario/100
#aumento = p*15
#novo_salario = salario+aumento

print('O seu novo salario é {:.2f}' .format(novo_salario))