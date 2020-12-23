#Jokenpo 
from random import randint
from time import sleep

itens = ['PEDRA','PAPEL','TESOURA']
vitorias = 0
derrotas = 0
empates = 0
escolha = 4
escolha_pc = randint(0,2)

while escolha != [0,1,2]:
    escolha = int(input('''\n---- Vamos Jogar! ----
Você pode escolher entre:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA\n'''))

    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!\n')
    sleep(1)

    if escolha == escolha_pc:
        print('Você escolheu {} e eu também escolhi {}, deu EMPATE! vamos tentar denovo'.format(itens[escolha],itens[escolha_pc]))
        empates += 1
        print(f'''\nVITORIAS {vitorias}
DERROTAS {derrotas}
EMPATES {empates}''')
        escolha = 4
    elif escolha == 0 and escolha_pc == 1 or escolha == 1 and escolha_pc == 2 or escolha == 2 and escolha_pc == 0:
        print(f'''Você esolheu {itens[escolha]}  
E eu escolhi {itens[escolha_pc]} 
GANHEI dessa vez! :D''')
        derrotas += 1
        print(f'''\nVITORIAS {vitorias}
DERROTAS {derrotas}
EMPATES {empates}''')
        escolha = 4
    else:
        print(f'''Você escolheu {itens[escolha]} 
E eu tinha escolhido {itens[escolha_pc]} 
Dessa vez eu PERDI :/''')
        vitorias += 1
        print(f'''\nVITORIAS {vitorias}
DERROTAS {derrotas}
EMPATES {empates}''')
        escolha = 4

