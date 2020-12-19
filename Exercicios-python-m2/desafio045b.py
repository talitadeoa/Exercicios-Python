#Jokenpo 
from random import randint
from time import sleep

itens = ['PEDRA','PAPEL','TESOURA']

escolha = int(input("""Vamos Jogar!
Você pode escolher: 
[0] PEDRA
[1] TESOURA
[2] PAPEL\n"""))
escolha_pc = randint(0,2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)


if escolha == escolha_pc:
    print('Você escolheu {} e eu também escolhi {}, deu empate! vamos tentar denovo'.format(itens[escolha],itens[escolha_pc]))
elif escolha == 0 and escolha_pc == 2 or escolha == 2 and escolha_pc == 1 or escolha == 1 and escolha_pc == 0:
    print('Você esolheu {} e eu escolhi {}, ganhei dessa vez! :D'.format(itens[escolha],itens[escolha_pc]))
else:
    print('Você escolheu {} e eu tinha escolhido {} dessa vez eu perdi :/'.format(itens[escolha],itens[escolha_pc]))

