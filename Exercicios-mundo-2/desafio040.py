#Um programa que lê duas notas e calcula se o aluno está reprovado, em recuperação ou aprovado

n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('E a segunda? '))
media = (n1+n2)/2

print('Ok, estou analisando...')

if media < 5:
    print('Foi mal, você está reprovado, sua média foi {}. Tente estudar mais na próxima! Boa sorte.'.format(media))
elif media >= 7:
    print('Parabéns! sua média foi {}, você está aprovado!'.format(media))
else:
    print('Sua média é {}, você está de recuperação, estude e boa sorte!'.format(media))