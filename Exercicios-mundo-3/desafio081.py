#Um programa que lê inputs int do usuario e armazena em uma lista, mostra quantos números foram inseridos, lista decrescente e se o número 5 está na lista

nums = []
hasfive = 0

while True:
    num = int(input('Qual número deseja adcionar? '))
    nums.append(num)
    print(f'Número {num} adcionado com sucesso! ')
    stop = ''
    while stop not in ['S','N']:
        stop = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if stop in 'N':
        break
nums.sort(reverse=True)
for i in nums:
    if i == 5:
        hasfive += 1

print(f'''\nVocê digitou {len(nums)} números
A lista de números em ordem decrescente é: {nums}
O número 5 foi inserido {hasfive} vezes''')
