#Programa que recebe os valores nome, data de nascimento e carteira de trabalho e calcula a idade, se a carteira de trabalho for diferente de 0 também recebe os valores de ano de contratação e salário e calcula a idade que o usuario irá se aposentar

from datetime import date
year = date.today().year

person = {'name': str(input("Qual seu nome ")), 'birth': int(input("Ano de nascimento ")), "ctps": int(input("Carteira de Trabalho (0 para não tem) "))}

person['age'] = (year-person['birth'])

if person['ctps'] > 0:
    person["hiring"] = int(input("Ano de contratação "))
    person["salary"] = int(input("Salário "))
    person["retiring"] = (person["age"]+35)

for k,v in person.items():
    print(f'{k}: {v}')

