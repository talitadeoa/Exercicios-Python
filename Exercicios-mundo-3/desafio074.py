#Um programa que cria uma tupla com números aletorios, lista-os e pontua o maior e menor.

from random import randint

a= randint(0,10)
b= randint(0,10)
c= randint(0,10)
d= randint(0,10)
e= randint(0,10)
menor = a
maior = a

tupla = (a,b,c,d,e)

for n in (tupla):
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(tupla)
print(f'maior: {maior}' )
print(f'menor: {menor}' )