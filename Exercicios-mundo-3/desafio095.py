#Aprimoramento do desafio 093, permmite cadastrar varios jogadores incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador 

team = []
player = dict()

while True:
    player.clear()     
    player = {'name': str(input('Nome: ')), 'matches': int(input('Partidas jogadas: ')), 'goals':[], 'total': 0}  
    for i in range(player['matches']):
        player['goals'].append(int(input(f'    Quantos gols na {i+1}ª partida ')))
        player['total'] = sum(player['goals'])
    team.append(player.copy())   
    
    while True:
        status = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if status in 'SN':
            break
        print('Por favor digite apenas S ou N.')
    if status == 'N':
        break   
    
print('-='*30)
print('cod ', end='')
for k in player.keys():
    print(f'{k:<15}', end='') 
print()    
print('--'*30)
for c, player in enumerate(team):
    print(f'{c:>3} ', end='')
    for d in player.values():
        print(f'{str(d):<15}', end='') 
    print()           
print('--'*30)
    
while True:
    pick = int(input('Para visualizar os dados de um jogador específico digite seu número (999 para finalizar) '))
    if pick == 999:
        break
    if pick > len(team):
        print(f'O/A jogador/a {pick} não existe, tente mais uma vez')
    else:
        print(f"Jogador/a {team[pick]['name']}")
    for i, g in enumerate(team[pick]['goals']):
        print(f'     Na partida {i+1} fez {g} gols')