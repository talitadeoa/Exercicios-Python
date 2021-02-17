#Um programa que lê numeros inseridos pelo usuario e adciona em uma lista se não forem repetidos, ao final mostra uma lista ordenada

nums = []

while True:
    num = int(input('Qual número deseja adcionar? '))
    if num not in nums:
        nums.append(num)
        print(f'Número {num} adcionado com sucesso! ')
    else:
        print(f'O número {num} já está na lista! Tente outra vez')
    stop = ''
    while stop not in ['S','N']:
        stop = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if stop in 'N':
        break
nums.sort()
print(nums)

