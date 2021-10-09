#Um programa que lê duas notas e calcula se o aluno está reprovado, em recuperação ou aprovado

n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('E a segunda? '))
average = (n1+n2)/2

print('Ok, estou analisando...')

if average < 5:
    print('Foi mal, você está reprovado, sua média foi {}. Tente estudar mais na próxima! Boa sorte.'.format(average))
elif average >= 7:
    print('Parabéns! sua média foi {}, você está aprovado!'.format(average))
else:
    print('Sua média é {}, você está de recuperação, estude e boa sorte!'.format(average))