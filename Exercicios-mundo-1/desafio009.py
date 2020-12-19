#Um programa que lê um número inteiro e mostra sua tabuada

numero = int(input('Digite um número inteiro... '))

item = 1



print('\n''Tabuada de adição:')
for item in range(11):
    print(numero,'+',item,'=',numero+item,)

print('-'*13)

print('\n''Tabuada de subtração:')
for item in range(numero,numero+11):
    print(item,'-',numero,'=',item-numero)

print('-'*13)

print('\n''Tabuada de multiplicação:')
for item in range(11):
    print(numero,'x',item,'=',item*numero)

print('-'*13)

print('\n''Tabuada de divisão:')
for item in range(1,11):
    print(numero,'/',item,'=',numero/item)

print('-'*13)