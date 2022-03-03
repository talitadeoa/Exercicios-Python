#Função contador que recebe 3 parametros, início, fim e passe, com exemplos e contador personalizado
#1 a 10 de 1 em 1
#10 a 0 de 2 em 2
#personalizado

from time import sleep

def contador(ini,fim,pas):
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}:')
    for i in range(ini,fim,pas):
        print(f'{i} ', end='')
        sleep(0.5)
    print('Fim!')

contador(1,10,1)
contador(10,0,2)