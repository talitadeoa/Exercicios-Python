#Programa que calcula o rendimento de um jogador de futebol, calculando quantas partidas ele jogou e a quantidade de gols por partida

player = {'name': str(input('Nome: ')), 'matches': int(input('Partidas jogadas: '))}
goals = []

for i in range(player['matches']):
    goals.append(int(input(f'Quantos gols na {i+1}ª partida ')))
    player['goals'] = goals[:]

print(f"\nO jogador {player['name']} participou em {player['matches']} partidas")
for i in range(player['matches']):
    print(f'Na {i+1}ª partida => {goals[i]} gols')
print(f'Totalizando {sum(player["goals"])} gols no campeonato')