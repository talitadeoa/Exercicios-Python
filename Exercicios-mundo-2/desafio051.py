#Um programa que lê o primeiro termo e a razão de uma progressão aritmétrica, e mostra os 10 primeiros termos dessa progressão

pt = int(input('Qual o primeiro termo da PA? '))
r = int(input('E qual a razão? '))
x = 10*r

for i in range (pt, x, r):
    print(i, end=' ')