#Um programa que lê nome e peso e ao final mostra quantas pessoas foram cadastradas, quais foram as mais pesadas e menos pesadas

temp = []
people = []
weight = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    people.append(temp[:])
    weight.append(temp[1])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Você cadastrou {len(people)} pessoas')
print(f'O maior peso foi de {max(weight):.2f}Kg. Peso de ', end='')
for p in people:
    if p[1] == max(weight):
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {min(weight):.2f}Kg. Peso de ', end='')
for p in people:
    if p[1] == min(weight):
        print(f'{p[0]} ', end='')