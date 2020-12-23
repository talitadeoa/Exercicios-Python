#Um programa que mostra o fatorial de um número


nn = int(input('Digite o número que deseja saber o fatorial '))
fatorial = 1
numero = nn

print(f'calculando {numero}! = ', end='')
while numero > 0:
    print(f'{numero} ', end='')
    print('x ' if numero > 1 else f'= {fatorial}', end= '')
    fatorial *= numero
    numero -= 1


#print(f'O fatorial {numero}! é {fatorial}')

