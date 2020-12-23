#Um programa que lê o sexo de uma pessoa e só aceita os valores M ou F

sexo = (input('Qual seu sexo? [M/F] ')).upper().strip()[0]

while sexo not in 'MF':
    sexo = (input('Dados inválidos, responda novamente [M/F] ')).upper().strip()[0]

if sexo == 'F':
    sexo = 'feminino'
else:
    sexo = 'masculino'

print(f'Sexo {sexo} registrado com sucesso')