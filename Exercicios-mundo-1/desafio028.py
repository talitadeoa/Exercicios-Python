#Um programa que escolhe um número de 0 a 5 e o usuário tenta advinhar
import random

n = int(input("Escolha um número entre 0 e 5... "))

escolha = random.randint(0,5)

if n == escolha:
    print("Parabéns o número escollhido foi {}! Você ganhou!".format(escolha))
else:
        print("O número escolhido foi {}, é uma pena, você perdeu... Tente novamente =D".format(escolha))

