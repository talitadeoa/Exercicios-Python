#Versao melhorada do exercicio 28

import random
    
palpite = int(input("Escolha um número entre 0 e 10... "))
pc = random.randint(0,10)
tentativas = 0

print(pc)

while palpite != pc:
    if palpite > pc:
        palpite = int(input('Menos... tente novamente: '))
        tentativas += 1
    elif palpite < pc:
        palpite = int(input('Mais... tente novamente: '))
        tentativas += 1

if palpite == pc:
    print(f'''Parabéns você acertou! :D 
foram {tentativas} tentativas''')
