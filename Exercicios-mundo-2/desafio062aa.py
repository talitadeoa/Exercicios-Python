#Refazer o desafio 61 com uma opção para mostrar mais 5 progressões

pt = int(input('Qual o primeiro termo da PA? '))
r = int(input('E qual a razão? '))
t = pt
count = 1
qtd = 10  #<total
vai = 1  #<mais
pro = 10

print('\n------ Gerador de PA ------ \n')

while vai != 0:
    qtd += vai
    while count <= qtd:
        print(f'{t} -> ', end='')
        t += r
        count += 1
    print('PAUSA')        
    vai = int(input('\nQuer mostrar mais quantos termos? Digite [0] para encerrar \n'))
print(f'\nOK, fim do programa, foram mostrados {qtd} termos')

