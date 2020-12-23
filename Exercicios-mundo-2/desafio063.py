#Programa que lê um número inteiro qualquer e mostra uma sequência fibonacci

#num = int(input('Digite um número inteiro qualquer_'))
qt = int(input('Quantos elementos você deseja ver?_'))
t1 = 0
t2 = 1

count = 3

print(f'{t1} -> {t2}', end='')

while count < qt:
    t3 = t1+t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    count += 1