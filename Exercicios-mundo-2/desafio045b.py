#Jokenpo 
from random import randint
from time import sleep

itens = ['PEDRA','PAPEL','TESOURA']
vitorias = 0
derrotas = 0
empate = 0
escolha = int()
escolha_pc = randint(0,2)

while escolha not in [0,1,2,3]:
    escolha = int(input("""Vamos Jogar!
    Você pode escolher: 
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA\n"""))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

if escolha == escolha_pc:
    print('Você escolheu {} e eu também escolhi {}, deu empate! vamos tentar denovo'.format(itens[escolha],itens[escolha_pc]))
    empate += 1
elif escolha == 0 and escolha_pc == 1 or escolha == 1 and escolha_pc == 2 or escolha == 2 and escolha_pc == 0:
    print('Você esolheu {} e eu escolhi {}, ganhei dessa vez! :D'.format(itens[escolha],itens[escolha_pc]))
    derrotas += 1
else:
    print('Você escolheu {} e eu tinha escolhido {} dessa vez eu perdi :/'.format(itens[escolha],itens[escolha_pc]))
    vitorias += 1

