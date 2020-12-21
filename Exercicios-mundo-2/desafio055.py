#Um programa que lê o peso de 5 pessoas e informa qual o maior e menor peso

peso = 0
pessoa = 1
maior = 0
menor = 0

for i in range(0,5):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(pessoa)))
    pessoa += 1

