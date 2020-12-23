#Um programa que mostra o fatorial de um número

#usando o for

numero = int(input('Digite o número que deseja saber o fatorial '))
fatorial = 0

while numero > 1:
    fatorial += numero*numero-1
    numero = numero - 1

print(f'O fatorial {numero}! é {fatorial}')

