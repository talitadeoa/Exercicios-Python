#Aprimoramento do desafio 093, permmite cadastrar varios jogadores incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador 

players = []

while True:
    player = {'name': str(input('Nome: ')), 'matches': int(input('Partidas jogadas: '))}
    goals = []
    for i in range(player['matches']):
        goals.append(int(input(f'Quantos gols na {i+1}ª partida ')))
        player['goals'] = goals[:]
    players.append(player.copy())    
    while True:
        status = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if status in 'SN':
            break
        print('Por favor digite apenas S ou N.')
    if status == 'N':
        break   


print(f"\nO jogador {player['name']} participou em {player['matches']} partidas")
for i in range(player['matches']):
    print(f'Na {i+1}ª partida => {goals[i]} gols')
print(f'Totalizando {sum(player["goals"])} gols no campeonato')