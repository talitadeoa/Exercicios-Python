#Um programa que lê 4 valores e coloca em uma tupla
#a) Quantas vezes aparece o 9
#b) Em que posição foi digitado o primeiro 3
#c) Quais os números pares

for i in range [a,b,c,d]:
    i= int(input('Qual '))

tupla = (a,b,c,d)

nine = tupla.count(9)

if tupla.count(3) == 0:
    f3 = 'nenhuma' 
else:
    f3 = tupla.index(3)+1

evens = []
odds = []

for n in tupla:
    if n % 2 == 0 and n != 0:
        evens.append(n)
#        print(n,',',end=' ')
    else:
        odds.append(n)

print(f'{tupla} \nO número 9 aparece {nine} \nA posição em que aparece o primeiro 3 é {f3} \nOs números pares são: {evens}' )