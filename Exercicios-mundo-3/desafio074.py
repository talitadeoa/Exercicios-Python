#Um programa que cria uma tupla com números aletorios, lista-os e pontua o maior e menor.

from random import randint

a= randint(0,10)
b= randint(0,10)
c= randint(0,10)
d= randint(0,10)
e= randint(0,10)

numbers = (a,b,c,d,e)

print(numbers)
print(f'maior: {max(numbers)}' )
print(f'menor: {min(numbers)}' )