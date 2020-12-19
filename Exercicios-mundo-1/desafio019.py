#Crie um programa que faz o sorteio de um aluno para limpar o quadro
import random

a1 = input("Quem é o primeiro aluno(a)? ")
a2 = input("Quem é o segundo aluno?(a) ")
a3 = input("Quem é o terceiro aluno?(a) ")
a4 = input("Quem é o quartp aluno?(a) ")

alunos = [a1,a2,a3,a4]

sorteado = random.choice(alunos)

print("O aluno(a) {} foi o escolhido para limpar o quadro".format(sorteado))