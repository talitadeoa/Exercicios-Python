#Um programa que calcula a soma de todos os números ímpares entre 1 e 500

s = 0
for i in range (1, 501):
    if i%2 != 0:
        s = i+i

print('A soma de todos os números ímpares entre 1 e 500 é {}'.format(s))