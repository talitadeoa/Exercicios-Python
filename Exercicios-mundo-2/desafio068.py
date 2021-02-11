#Um programa que joga par ou impar, mas que o jogo só para quando o usuario perde, ao final mostra quantas vitorias consecutivas teve

from random import randint

number = victories = result = 0
pc_number = randint(0,10)
pi = ''
perdeu = False

while perdeu is False:
    while pi not in ['P','I']:
        pi = input('Par ou Ímpar? [P/I] ').upper()
    if pi == 'P':
        pi = 'PAR'
    elif pi == "I":
        pi = 'ÍMPAR'
    number = int(input('Digite um número... '))
    result = pc_number+number
    if pi == 'PAR' and result%2 == 0:
        print(f'Você jogou {number} e o pc {pc_number}, {result} é {pi}, você ganhou! ')
        victories += 1  
    elif pi == 'ÍMPAR' and result%2 != 0:
        print(f'Você jogou {number} e o pc jogou {pc_number}, {result} é {pi}, você ganhou! ')
        victories += 1
    else:
        print(f'Você jogou {number} e o pc jogou {pc_number}, {result} não é {pi}, você perdeu ')
        perdeu = True

print(f'Você teve {victories} vitórias consecutivas!')

    