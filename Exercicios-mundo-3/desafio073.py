#Um programa que lê os times do brasileirão e informa:
#a) Os 5 primeiros
#b) Os 4 últimos colocados
#c) Ordem alfabética
#d) Em qual posição tá o time x
	
brasileirao = ('Internacional', 'Flamengo', 'Atlético-MG','São Paulo','Fluminense' ,'Grêmio' ,'Palmeiras', 'Santos', 'Corinthians', 'Bragantino', 'Athletico-PR', 'Ceará', 'Atlético-GO', 'Sport', 'Fortaleza', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')

option = ''
resume = ''

while option not in ['a','b','c','d']:
    option = input('''O que você deseja saber?  
a) Os 5 primeiros
b) Os 4 últimos colocados
c) Ordem alfabética
d) Em qual posição tá o time x
''').strip().lower()[0]

if option == 'a':
    print(brasileirao[:5])
elif option == 'b':
    print(brasileirao[-4:])
elif option == 'c':
    print(sorted(brasileirao))
elif option == 'd':
    team = input('Qual time você deseja saber a posição? ')
    pos = brasileirao.index(team)
    print(f'O time {team} está na posição {pos+1}')

while resume not in ['S','N']:
    resume = ('Deseja voltar para o menu? [S/N]').upper().strip()[0]
if resume == 'S':
    option = ''
else:
    print('Encerrando...')
    