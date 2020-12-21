#Um programa que recebe 7 valores de ano de nascimento e retorna quantos já chegaram a maioridade e quantos ainda não

from datetime import date

year = 0
count = 1
plus18 = 0
less18 = 0
c_year = date.today().year
plus = []
less = []

for i in range (0,7):
    year = int(input('Qual o {}º ano de nascimento? '.format(count)))
    count += 1
    if c_year - year >= 18:
        plus18 += 1
    else:
        less18 += 1

print()

