#Um programa que lê idade e sexo de várias pessoas no final informa quantos sao maiores de 18, quantos são homens e quantas mulheres tem menos de 20 anos

p = age = 0
gender = ''
ages = []
genders = []
p18 = []
man = []
wlt20 = []
stop = False

while stop is not True:
    age = int(input(f'Digite a idade da {p+1}ª pessoa: '))
    while age < 0:
        age = int(input(f'Digite a idade da {p+1}ª pessoa: '))        
    ages.append(age)
    gender = (input(f'Digite o sexo da {p+1}ª pessoa: [M/F] ').upper())
    while gender not in ['M','F']:
        gender = (input(f'Digitde o sexo da {p+1}ª pessoa: [M/F] ').upper())
    genders.append(gender)
    p+=1
    stop = input('Deseja continuar? [S/N] ').upper()
    if stop == 'N':
        stop = True

print(f'{ages} \n {genders}')

#print(f'{len(p18)} Pessoas são maiores de 18 anos \n{len(man)} São homens \n{len(wlt20)} São mulheres com menos de 20')


    