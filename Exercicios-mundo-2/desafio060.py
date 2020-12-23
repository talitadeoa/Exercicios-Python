#Um programa que mostra o fatorial de um número

from math import factorial

n = int(input('Qual o número que deseja saber o fatorial? '))
f = factorial(n)

print(f'O fatorial de {n}! é {f}')