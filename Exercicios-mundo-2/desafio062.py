#Refazer o desafio 61 com uma opção para mostrar mais 5 progressões

pt = int(input('Qual o primeiro termo da PA? '))
r = int(input('E qual a razão? '))
t = pt
count = 1
qtd = 10
vai = 0

while vai != 0:
    while count <= qtd:
        print(f'{t} -> ', end='')
        t += r
        count += 1
        vai = int(input('Quer ir dnv(mostra mai 5)? sim[1] nao[0]'))
    if vai == 1:
        qtd +=5
    elif vai == 0:
        print('fim')
    else:
        print('Po mano tu n digitou os dados certo, roda dnv aí entaão se quiser...')            

