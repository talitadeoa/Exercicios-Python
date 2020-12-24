#Um programa que recebe vários valores inteiros. Ao final mostra a média entre eles, o maior e menor e pergunta se ele quer ou não continuar inserindo valores

num = int()
media = 0
maior = 0
menor = 0
count = 0
state = 'S'
soma = 0

while state == 'S':
    num = int(input('Digite um número inteiro '))  
    count += 1
    soma += num   
    if count == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    state = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while state not in 'SN':
        state = input('Deseja continuar? [S/N]: ').strip().upper()[0]    

media = soma / count
print(f' Você digitou {count} valores, \n A média entre eles é {media} \n O maior valor é {maior} \n E o menor {menor}')

