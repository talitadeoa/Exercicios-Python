#Função que cria um mini-sistema para utilizar o interactive help

from time import sleep

cores = ('\033[m',  # sem cores
         '\033[1;97;46m', #cyan
         '\033[1;32;47m', #verde e cinza
         '\033[1;97;45m',  # roxo
         '\033[1;37;43m',  # amarelo
         '\033[7;30;107m'  # branco e preto
         '\033[0;36;47m', #verde e cinza         
         )

def tit(txt,cor=0):
    bar = int(len(txt)*2)
    print(cores[cor])
    print('='*bar)
    print(f'{txt:^{bar}}')
    print('='*bar)
    print(cores[2])
        
def pyhelp():
    while True:
        tit("Sistema de ajuda PyHelp",1)
        cmd = input("Função ou biblioteca >> ").strip()
        if cmd.upper() == 'END':
            tit("Obrigada por usar o PyHelp, xauzin",3)    
            break      
        tit(f"Acessando o manual de \'{cmd}\'...",4)
        help(cmd)
pyhelp()