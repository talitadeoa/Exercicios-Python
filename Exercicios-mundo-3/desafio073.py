#Um programa que lê os times do brasileirão e informa:
#a) Os 5 primeiros
#b) Os 4 últimos colocados
#c) Ordem alfabética
#d) Em qual posição tá o time x
	
brasileirao = ('Internacional', 'Flamengo', 'AtléticoMG',' São Paulo','Fluminense' ,'Grêmio' ,'Palmeiras', 'Santos', 'Corinthians', 'Bragantino', 'AthleticoPR', 'Ceará', 'AtléticoGO', 'Sport', 'Fortaleza', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')

option = ''

while option not in 'abcd':
    option = input('''O que você desejaa saber?  
a) Os 5 primeiros
b) Os 4 últimos colocados
c) Ordem alfabética
d) Em qual posição tá o time_\n
''').strip().lower()[0]

if option == 'a':
    print(brasileirao[:6])
elif option == 'b':
    print(brasileirao[-5:])
elif option == 'c':
    print(sorted(brasileirao))
