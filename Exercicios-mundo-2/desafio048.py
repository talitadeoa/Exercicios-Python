#Um programa que calcula a soma de todos os números ímpares entre 1 e 500

soma = 0
count = 0
for i in range (1, 501, 2):
    if i % 3 == 0:
        soma+=i
        count+=1

print('A soma dos {} valores ímpares múltiplos de 3 entre 1 e 500 é {}'.format(count,soma))
