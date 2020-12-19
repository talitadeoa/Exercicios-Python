#Jokenpo 
from random import randint

print('Pedra, papel ou tesoura? ')

escolha = int(input("""Para escolher pedra digite [0]
Para escolher teroura digite [1]
Para escolher papel digite [2]\n"""))

escolha_pc = randint(0,2)

if escolha_pc == 0:
    escolha_pc = 'pedra'
elif escolha_pc == 1:
    escolha_pc = 'papel' 
else:
    escolha_pc = 'tesoura'

if escolha == 0:
    escolha = 'pedra'
elif escolha == 1:
    escolha = 'papel' 
else:
    escolha = 'tesoura'

if escolha == escolha_pc:
    print('Você escolheu {} e eu também escolhi {}, deu empate! vamos tentar denovo'.format(escolha,escolha_pc))
elif escolha == 'pedra' and escolha_pc in 'papel' or escolha == 'papel' and escolha_pc in 'tesoura' or escolha == 'tesoura' and escolha_pc in 'pedra':
    print('Você esolheu {} e eu escolhi {}, ganhei dessa vez! :D'.format(escolha,escolha_pc))
else:
    print('Você escolheu {} e eu tinha escolhido {} dessa vez eu perdi :/'.format(escolha,escolha_pc))