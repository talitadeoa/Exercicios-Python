#Um programa que lê 6 números inteiros e mostra a soma dos números pares, desconsiderando os números ímpares

s = 0
count = 6
countp = 0

for i in range (0,count):
    ni = int(input('Digite um número inteiro '))
    if ni % 2 == 0:
        s += ni
        countp += 1

print('A soma dos {} números pares digitados é {}, foram descartados {} números ímapres'.format(countp,s,count-countp))
