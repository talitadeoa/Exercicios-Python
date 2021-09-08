#Um programa que cria uma tupla com números aletorios, lista-os e pontua o maior e menor.

from random import randint

numbers = ((randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10)))

print(f'Os números selecionados foram:', end='')
for n in numbers:
    print(f'{n} ', end='')
print(f'\nmaior: {max(numbers)}' )
print(f'menor: {min(numbers)}' )