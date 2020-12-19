#Um programa que lê a idade de um atleta e mostra sua classificação

idade = int(input('Quantos anos você tem? '))

if idade <= 9:
    print('Sua classificação é: mirim')
elif idade <= 14:
    print('Sua classificação é: infantil')
elif idade <= 19:
    print('Sua classificação é: junior')
elif idade <= 20:
    print('Sua classificação é: senior')
else:
    print('Sua classificação é: master')