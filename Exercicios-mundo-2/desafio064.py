#Um programa que lê vários números até receber 999(condição de parada) Mostra quantos valores foram inseridos e a soma deles

num = 0
count= 0
all = []
sum1 = 0
sum2 = 0
vav = 0 

while num != 999:
    num = int(input('Digite um número inteiro qualquer (999 para parar) '))
    if num != 999:
        count += 1
        sum1 += num 
        all.append(num)

    while vav < (len(all)):
        sum2 += all[vav] 
        vav += 1

print(f'Ok, você inseriu {count} valores, sendo eles {all} a soma total é {sum1}')
