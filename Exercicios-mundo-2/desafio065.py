#Um programa que recebe vários valores inteiros. Ao final mostra a média entre eles, o maior e menor e pergunta se ele quer ou não continuar inserindo valores

num = int()
media = 0
maior = 0
menor = 0
count = 0
state = 'S'

while state == 'S':
    num = int(input('Digite um número inteiro '))  
    count += 1
    media += num / count
    maior = num
    menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    state = '0'

    while state not in 'SN':
        state = input('Deseja continuar? [S/N]: ').strip().upper()  

print(f' Você digitou {count} valores, \n A média entre eles é {media} \n O maior valor é {maior} \n E o menor {menor}')

