#Um programa que joga par ou impar, mas que o jogo só para quando o usuario perde, ao final mostra quantas vitorias consecutivas teve

from random import randint

number = victories = result = 0
pc_number = randint(0,10)
eo = ''
mood = True

while mood:
    while number != [0:10]:
        number = int(input('Digte um número '))
    while eo not in ['P','I']:
        eo = input('Par ou Ímpar? [P/I] ').upper()
    result = pc_number+number
    if eo =='P':
        if result%2 == 0:
            print(f'Você jogou {number} e o pc {pc_number} deu PAR, você ganhou!')
            victories += 1
        else:
            print(f'Você jogou {number} e o pc {pc_number} deu ÍMPAR! Você perdeu')    
    elif eo == 'I':
        if result%2 != 0:
            print(f'Você escolheu {number} e o pc escolheu {pc_number} deu ÍMPAR, você ganhou!')
            victories += 1
            mood = False
        else:
            print(f'Você jogou {number} e o pc {pc_number} deu PAR! Você perdeu \n você teve {victories} vitórias consecutivas')
            mood = False
    