#Programa que simula um jogo de dados, sorteando números aleatórios para 4 jogadores, os dados são armazenados em um dicionário ordenado que é apresentado ao fim do programa

from random import randint
from operator import itemgetter

game = {'player1' : randint(1,6),'player2' : randint(1,6),'player3' : randint(1,6),'player4' : randint(1,6)}
ranking = []

print("Números sorteados: ")

for k, v in game.items():
    print(f'{k} tirou {v}')

ranking = sorted(game.items(), key = itemgetter(1), reverse = True)
print('-='*30)
print('Ranking:')
for i, v in enumerate(ranking):
    print(f'{v[0]}: {v[1]}')
#    if player['score'] > 0:

#for i in sorted(d, key = .get, reverse=True):
#    print(i, d[i])
