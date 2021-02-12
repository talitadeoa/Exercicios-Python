#Um programa que mostra atabuada de um inteiro qualquer digitado pelo usuário, o programa é encerrado quando o valor inserido for negativo

n = result = count = 0

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n <= 0:
        break
    print(f'\nA tabuada de {n} é:')
    while count <= 10:
        result = n*count
        print(f'{n} x {count} = {result}')
        count += 1
    print('-'*20)
    count = 0
print('\nEncerrando tabuada')