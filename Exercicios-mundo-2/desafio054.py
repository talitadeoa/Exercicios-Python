#Um programa que recebe 7 valores de ano de nascimento e retorna quantos já chegaram a maioridade e quantos ainda não

from datetime import date

maioridade = 18
year = 0
count = 1
plusm = 0
lessm = 0
c_year = date.today().year
plus = []
less = []

for i in range (0,7):
    year = int(input(f'Qual o {i+1}º ano de nascimento? '))
    count += 1
    if c_year - year >= maioridade:
        plus18 += 1
        plus.append(year)
    else:
        less18 += 1
        less.append(year)

print('''Com os dados informados pude analisar que dos 7 anos inseridos {} já atingiram a maioridade sendo eles: {} 
E {} ainda são de menor sendo eles: {}'''.format(plusm,plus,lessm,less))


