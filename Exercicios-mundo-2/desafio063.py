#Programa que lê um número inteiro qualquer e mostra uma sequência fibonacci

num = int(input('Digite um número inteiro qualquer_'))
qt = int(input('Quantos elementos você deseja ver?_'))
pro = 0
a = num - 1
aa = num - 2

while num < 1 or a < 1 or aa < 1:
    num += 1

while qt > 0:
    print(f'{num}', end=' ')
    num += a + aa
    qt -= 1


