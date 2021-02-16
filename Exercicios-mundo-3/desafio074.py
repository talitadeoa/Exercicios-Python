#Um programa que cria uma tupla com números aletorios, lista-os e pontua o maior e menor.

from random import randint

a= randint(0,10)
b= randint(0,10)
c= randint(0,10)
d= randint(0,10)
e= randint(0,10)

tupla = (a,b,c,d,e)

print(tupla)
print(f'maior: {max(tupla)}' )
print(f'menor: {min(tupla)}' )