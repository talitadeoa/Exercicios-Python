#Uma função ficha que recebe os dados do jogador, nome e quantidade de gols

def ficha(nome='', gol=''):
    if nome == '':
        nome = 'DESCONHECIDO'
    if not gol.isdigit():
        gol = 0
    print(f'O/A jogador/a {nome} fez {gol} gols no campeonato')


nome = input('Nome do/a Jogador/a: ').strip().title()
gols = input('Nº de gols: ').strip()

ficha(nome, gols)
