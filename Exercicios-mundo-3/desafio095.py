#Aprimoramento do desafio 093, permmite cadastrar varios jogadores incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador 

team = []
player = dict()

while True:
    player = {'name': str(input('Nome: ')), 'matches': int(input('Partidas jogadas: ')), 'goals':[], 'total': 0}  
    for i in range(player['matches']):
        player['goals'].append(int(input(f'Quantos gols na {i+1}ª partida ')))
        player['total'] = sum(player['goals'])
    team.append(player.copy())   
    player.clear() 
    while True:
        status = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if status in 'SN':
            break
        print('Por favor digite apenas S ou N.')
    if status == 'N':
        break   
    
print('-='*21)
print('cod ', end='')
for k in player.keys():
    print('{i:<15}', end='') 
print()    
print('-'*42)
for c, player in enumerate(team):
    print(f'{c:>4}', end='')
    for d in player.values():
        print(f'{str(d):<15}', end='') 
    print()           
print('-----')
