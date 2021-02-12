#Um programa que lê idade e sexo de várias pessoas no final informa quantos sao maiores de 18, quantos são homens e quantas mulheres tem menos de 20 anos

p = 1
ages = []
genders = []
p18 = []
men = []
wlt20 = []

while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA')
    print('-' * 25)
    age = int(input(f'Digite a idade da {p}ª pessoa: '))
    while age < 0:
        age = int(input(f'Digite a idade da {p}ª pessoa: '))        
    ages.append(age)
    gender = ''
    while gender not in ['M','F']:
        gender = (input(f'Digitde o sexo da {p}ª pessoa: [M/F] ').upper().strip()[0])
    genders.append(gender)

    if gender == 'M':
        men.append(p)
    if age >= 18:
        p18.append(p)
    if gender == 'F' and age < 20:
        wlt20.append(p)
    stop = ''
    while stop not in ['S','N']:
        stop = input('Deseja continuar? [S/N] ').upper()[0]
    if stop == 'N':
        break
    else:
        p+=1

print(f'\n{len(p18)} Pessoas são maiores de 18 anos \n{len(men)} São homens \n{len(wlt20)} São mulheres com menos de 20')


    