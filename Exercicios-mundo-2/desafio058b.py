#Versao melhorada do exercicio 28

import random
    
palpite = int(input("Escolha um número entre 0 e 10... "))
pc = random.randint(0,10)
tentativas = 0
acertou = False

while not acertou:
    if palpite == pc:
        acertou = True
    elif palpite > pc:
        palpite = int(input('Menos... tente novamente: '))
        tentativas += 1
    elif palpite < pc:
        palpite = int(input('Mais... tente novamente: '))
        tentativas += 1

print(f'''Parabéns você acertou! :D 
foram {tentativas} tentativas''')
