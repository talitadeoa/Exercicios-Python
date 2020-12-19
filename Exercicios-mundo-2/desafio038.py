#Um programa que lê dois número e fala qual é maior e menor

n1 = float(input('Digite o primeiro número... '))
n2 = float(input('Agora digite o segundo número... '))

if n1 > n2:
    print('O número {} é maior que {}'.format(n1,n2))
elif n2 > n1:
    print('O número {} é maior que {}'.format(n2,n1))
else:
    print('Os números são idênticos')