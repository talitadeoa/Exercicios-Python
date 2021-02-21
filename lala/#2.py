#Programinha que calcula horas
#Transformar em função
#opção de fazer com hrs e n so minutos

nowh = int(input('Que horas são? '))
nowm = int(input('Que minutos são? '))
plus = less
option = int(input('Deseja saber que horas são [+] ou [-]? [1/0] '))

if option == 1:
    plus == int(input('Deseja adcionar quantos minutos? '))
    if nowm + plus >= 60:
        nowh + 1
        if nowm + plus - 60 > 0:
            resm = nowm + plus - 60
elif option == 0:
    less == int(input('Deseja tirar quantos minutos? '))
    if nowm - less >= 0:
        nowh - 1
###        if nowm + less - 60 > 0:
            resm = nowm + less - 60    