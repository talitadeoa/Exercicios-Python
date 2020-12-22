#Um programa que lê o peso de 5 pessoas e informa qual o maior e menor peso

pesos = []
peso = 0
pessoa = 1
maior = 0
menor = 0

for i in range(0,5):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(pessoa)))
    pessoa += 1
    pesos.append(peso)

if pesos[0] > pesos[1] and pesos[0] > pesos[2] and pesos[0] > pesos[3] and pesos[0] > pesos[4]:
    print('O peso {} é o maior peso da lista'.format(pesos[1]))
if pesos[1] > pesos[0] and pesos[1] > pesos[2] and pesos[1] > pesos[3] and pesos[1] > pesos[4]:
    print('O peso {} é o maior peso da lista'.format(pesos[2]))
if pesos[2] > pesos[1] and pesos[2] > pesos[3] and pesos[2] > pesos[4] and pesos[3] > pesos[5]:
    print('O peso {} é o maior peso da lista'.format(pesos[3]))
if pesos[4] > pesos[1] and pesos[4] > pesos[2] and pesos[4] > pesos[3] and pesos[4] > pesos[5]:
    print('O peso {} é o maior peso da lista'.format(pesos[4]))
if pesos[5] > pesos[1] and pesos[5] > pesos[2] and pesos[5] > pesos[3] and pesos[5] > pesos[4]:
    print('O peso {} é o maior peso da lista'.format(pesos[5])) 

print(peso)
print(pesos)