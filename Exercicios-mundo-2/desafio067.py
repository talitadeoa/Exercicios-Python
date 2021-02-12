#Um programa que mostra atabuada de um inteiro qualquer digitado pelo usuário, o programa é encerrado quando o valor inserido for negativo

n = result = count = 0

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    print(f'A tabuada de {n} é:')
    for count in range(1,11):
        result = n*count
        print(f'{n} x {count} = {result}')
    print('-'*20)
print('\nEncerrando tabuada')