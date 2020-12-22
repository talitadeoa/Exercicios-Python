#Versao melhorada do exercicio 28

import random

n = int()
escolha = random.randint(0,5)
tentativas = 0

while n != escolha:
    n = int(input("Escolha um número entre 0 e 5... "))
    tentativas += 1

if n == escolha:
    print(f'''Parabéns você acertou! :D 
foram {tentativas} tentativas''')