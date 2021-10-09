#Programa que recebe dados de várias pessoas, como nome, idade e sexo, por fim cria uma lista e informa a quantidade de pessoas cadastradas, as mulheres e a média da idade entre elas e lista as pessoas com idade acima da média

person= {}
people = []
status = '0'
sum = media = 0
acima_media = []

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
media = (sum/len(person)) 

print(f'''Foram cadastradas {len(person)} pessoas
A média de idade entre elas é {media:.1f} anos
As mulheres cadastradas são 
As pessoas que tem idade acima da média são: ''', end='')
for p in person:
    if person[i]['age'] > media:
        acima_media.append(person[i]['name'].copy())    

print(acima_media)