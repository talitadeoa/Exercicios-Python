#Um programa que analisa um solicitação de empréstimo imobiliario com base no salário, valor da casa e número de parcelas

salario = float(input('Qual é o seu salário? R&'))
casa = float(input('Qual é o valor da casa? R$'))
anos = int(input('Em quantos anos você deseja pagar? '))
prestacao = casa / (anos*12)
salario_30 = salario * 30/100

if prestacao <= salario_30:
    print('O valor da sua prestação mensal será R${:.2f}'.format(prestacao))
else:
    print('Sinto muito, você não pode solicitar esse empréstimo no momento.')

