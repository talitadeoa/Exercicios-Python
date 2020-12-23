#Refaça o desafio 051 usando o while

pt = int(input('Qual o primeiro termo da PA? '))
r = int(input('E qual a razão? '))
t = pt
count = 1

while count <= 10:
    print(f'{t} -> ', end='')
    t += r
    count += 1
print('fim')