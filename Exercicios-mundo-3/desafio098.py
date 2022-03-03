#Função contador que recebe 3 parametros, início, fim e passe, com exemplos e contador personalizado
#1 a 10 de 1 em 1
#10 a 0 de 2 em 2
#personalizado

from time import sleep

def linha():
    print('--'*20)
    
def contador(ini,fim,pas):
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}:')
    if ini < fim:
        for i in range(ini,fim,pas):
            print(f'{i} ', end='', flush=True)
            sleep(0.5)
        print('Fim!')
    else:
        cont = ini
        while cont 

contador(1,10,1)
contador(10,0,2)
linha()
print('Agora é sua vez de escolher a contagem!')
contador(int(input('Início:')),int(input('Fim:')),int(input('Passe:')))
