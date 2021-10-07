#Programa que sorteia números aleatórios para 4 jogadores, os dados são armazenados em um dicionário ordenado que é apresentado ao fim do programa

import random

game = []
player = {}

print("Números sorteados: ")

for i in range(1,5):
    player['score'] = random.randint(1,6)
    print(f'O jogador {i} tirou {player["score"]}')
#    if player['score'] > 0:

for i in sorted(d, key = d.get, reverse=True):
    print(i, d[i])
