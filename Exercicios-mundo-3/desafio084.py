#Um programa que lê nome e peso e ao final mostra quantas pessoas foram cadastradas, quais foram as mais pesadas e menos pesadas
#Tente outra forma usando o clear

people = []
weights = []
heaviest = 0
thinner = 0
person = 1
thin = []
fatty  = []

while True:
    name = str(input(f'Digite o nome da {person}ª pessoa '))
    people.append(name)
    weight = int(input(f'Digite o peso da {person}ª pessoa '))
    weights.append(weight)
    if weight > heaviest:
        heaviest = weight
    for count, w in enumerate(weights):
         if w == heaviest:
            fatty.append(people[count])
    stop = ''
    while stop not in ['S','N']:
        stop = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if stop in 'N':
        break
    person += 1
print(f'''Foram adcionadas {person} pessoas
A mais pesada tem {heaviest} Kg. São: {fatty} ''')