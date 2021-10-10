#Aprimoramento do desafio 093, permmite cadastrar varios jogadores incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador 

players = []

while True:
    player = {'name': str(input('Nome: ')), 'matches': int(input('Partidas jogadas: ')), 'goals': [0], 'total': 0}  
    for i in range(player['matches']):
        player['goals'].append(int(input(f'Quantos gols na {i+1}ª partida ')))
        player['total'] = sum(player['goals'])
    players.append(player.copy())    
    while True:
        status = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if status in 'SN':
            break
        print('Por favor digite apenas S ou N.')
    if status == 'N':
        break   
print('-='*21)
print(f'{"Cod ":>4}{"Nome":<10}{"Gols ":<16}{"Total":<2}')
print('-'*42)
for i, player in enumerate(players):
    print(f'{i:>4}{player["name"]:<10}{player["goals"]}{player["total"]}')


