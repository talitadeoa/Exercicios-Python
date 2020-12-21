#Um programa que lê um número inteiro e informa se ele é ou não primo

n = int(input('Digite um número inteiro: '))
t = 0
for i in range(1, n+1):
    if n % i == 0:
        print('\033[33m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(i), end= ' ')
print('\n\033[mO número {} foi dividido {} vezes'.format(n,t))
if t == 2:
    print('E por isso é um número primo')
else:
    print('E Por isso não é um número primo')
