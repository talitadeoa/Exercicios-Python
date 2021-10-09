#Programa que recebe dados de várias pessoas, como nome, idade e sexo, por fim cria uma lista e informa a quantidade de pessoas cadastradas, as mulheres e a média da idade entre elas e lista as pessoas com idade acima da média

person= {}
people = []
status = '0'
sum = average = 0
woman = []
above_average = []

while True:
    person['name'] = str(input('Nome: '))
    person['age'] = int(input('Idade: '))
    sum += person['age']
    while True:
        person['sex'] = str(input('Sexo [F/M]: ')).upper()[0]
        if person['sex'] in 'FM:':
            break
        print('Por favor digite apenas M ou F.')
    person.append(person.copy())
    while True:
        status = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if status in 'SN':
            break
        print('Por favor digite apenas S ou N.')
    if status == 'N':
        break
average = (sum/len(person)) 

print(f'''Foram cadastradas {len(person)} pessoas
A média de idade entre elas é {average:.1f} anos
As mulheres cadastradas são 
As pessoas que tem idade acima da média são: ''', end='')
for p in people:
    if person[i]['age'] > average:
        above_average.append(person[i]['name'].copy())    

print(above_average)