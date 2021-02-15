#Um programa que lê 4 valores e coloca em uma tupla
#a) Quantas vezes aparece o 9
#b) Em que posição foi digitado o primeiro 3
#c) Quais os números pares

from random import randint

a= randint(0,10)
b= randint(0,10)
c= randint(0,10)
d= randint(0,10)

tupla = (a,b,c,d)

nine = tupla.count(9)

for n in tupla:
    if n == 3:
        f3 = tupla.index(3)
    elif:
        f3 = 'nenhuma' 

evens = []
odds = []

for n in tupla:
    if n % 2 == 0 and n is not 0:
        evens.append(n)
    else:
        odds.append(n)

print(f'{tupla} \nO número 9 aparece {nine} \nA posição em que aparece o primeiro 3 é {f3} \nOs números pares são: {evens}' )