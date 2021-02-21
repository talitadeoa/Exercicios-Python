#Um programa que recebe varios valores, os lista e separa pares e ímpares

nums = []
odd = []
evens = []

while True:
    num = int(input('Qual número deseja adcionar? '))
    nums.append(num)
    print(f'Número {num} adcionado com sucesso! ')
    stop = ''
    while stop not in ['S','N']:
        stop = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if stop in 'N':
        break

for i, num in enumerate(nums):
    if num % 2 == 0:
        evens.append(num)
    else: 
        odd.append(num)

print(f'''Números digitados {nums}
Números pares: {evens}
Números ímpares: {odd}''')
