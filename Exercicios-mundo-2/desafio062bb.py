#Refazer o desafio 61 com uma opção para mostrar mais 5 progressões

pt = int(input('Qual o primeiro termo da PA? '))
r = int(input('E qual a razão? '))
t = pt
count = 1
qtd = 10
vai = 1
pro = 10

print('------ Gerador de PA ------ ')

while vai != 0:
    while count <= qtd:
        print(f'{t} -> ', end='')
        t += r
        count += 1
    print('PAUSA')        
    vai = int(input('\nQuer mostrar mais quantas progessões? Digite [0] para encerrar '))
    if vai != 0:
        qtd += vai
        pro += vai
    elif vai == 0:
        print(f'\nOK, fim do programa, foram mostradas {pro} progessões')
    else:
        print('\nPo mano tu n digitou os dados certo, roda dnv aí então se quiser...')            

