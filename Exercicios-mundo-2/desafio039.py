#Um programa que lê a data de nascimento e calula a previsão para o alistamento
from datetime import date

ano_atual = date.today().year
genero = int(input('Qual o seu genero? Digite 0 para homem e 1 para mulher '))

if genero == 1:
    print('Você é mulher, não precisa fazer o alistamento! =)')

else:
    ano_nascimento = int(input('Qual ano você nasceu? '))
    idade = ano_atual - ano_nascimento
    if 18-idade == 1:
        print('Falta 1 ano para você ter de se alistar!')
    elif idade < 18:
        saldo = 18-idade
        ano = ano_atual+saldo
        print('Faltam {} anos para você ter de se alistar!'.format(saldo))
        print('Seu alistamento será em {}'.format(ano))
    elif idade == 18:
        print('Você deve se alistar já!')
    elif idade - 18 == 1:
        print('Já se passou 1 ano desde que você devia ter se alistado!')
    else:
        saldo = idade-18
        ano = ano_atual-saldo
        print('Já se passaram {} anos desde que você devia ter se alistado!'.format(saldo))
        print('Seu alistamento foi em {}'.format(ano))