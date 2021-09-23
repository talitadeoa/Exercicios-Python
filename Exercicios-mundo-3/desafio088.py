#Gerador de apostas da mega-sena. Um programa que gera x listas com 6 posições de inteiros de 1 a 60. 

from random import randint 
import time

bets = int(input('Quantas apostas deseja gerar? '))
bet = []
temp = []

print()
for i in range(0,bets):
    while len(temp) != 6:
        num = randint(1,60)
        if num not in temp:
            temp.append(num)
    temp.sort()        
    bet.append(temp[:])
    temp.clear()
    time.sleep(0.7)
    print(f'Jogo {i+1}: {bet[i]}')
