#Um programa que lê o sexo de uma pessoa e só aceita os valores M ou F

sexo = ''

while sexo not in ['M','F']:
    sexo = (input('Qual seu sexo? [M/F] ')).upper()

print(sexo)